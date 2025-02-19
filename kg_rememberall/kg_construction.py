#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CITATIONS and APPRECIATION:
- Paco Nathan:  a rework of code he originally shared during GraphGeeks.org talk 2024-08-14.
  - REPO URL:  https://github.com/DerwenAI/strwythura/blob/main/demo.py
- GLiNER:  https://arxiv.org/abs/2311.08526
- GLiREL:  https://arxiv.org/abs/2501.03172
"""

from collections import defaultdict
from dataclasses import dataclass
import enum
import itertools
import json
import logging
import math
import os
import pathlib
import sys
import typing
import unicodedata
import warnings

from bs4 import BeautifulSoup
from gliner_spacy.pipeline import GlinerSpacy
from icecream import ic
from lancedb.embeddings import get_registry
from lancedb.pydantic import LanceModel, Vector
import gensim
import glirel
import lancedb
import networkx as nx
import numpy as np
import pandas as pd
import pyvis
import requests
import spacy
import transformers
from prefect import flow, task
from prefect.logging import get_run_logger

######################################################################
## define the model selections and parameter settings

CHUNK_SIZE: int = 1024

EMBED_MODEL: str = "BAAI/bge-small-en-v1.5"

EMBED_FCN: lancedb.embeddings.transformers.TransformersEmbeddingFunction = \
    get_registry().get("huggingface").create(name = EMBED_MODEL)

#GLINER_MODEL: str = "urchade/gliner_small-v2.1"
GLINER_MODEL: str = "urchade/gliner_large-v2"

LANCEDB_URI = "../data/lancedb"

NER_LABELS: typing.List[str] = [
    "PERSON",        # For military/political leaders like Churchill, General Weygand, King Leopold
    "ORG",          # For organizations like Royal Air Force, Royal Navy, British Expeditionary Force  
    "GPE",          # For geopolitical entities like Belgium, France, England
    "LOC",          # For locations like beaches, channels
    "FACILITY",     # For facilities like ports, fortifications
    "DATE",         # For temporal references
    "EVENT",        # For battles and military operations
    "PRODUCT",      # For military equipment/vehicles (e.g. Spitfire, Hurricane)
    "NORP",         # For nationalities/religious/political groups (e.g. German, British, French)
]

RE_LABELS: dict = {
    "glirel_labels": {
        "commands": {
            "allowed_head": ["PERSON"], 
            "allowed_tail": ["ORG"]
        },
        "located_in": {
            "allowed_head": ["FACILITY", "LOC"], 
            "allowed_tail": ["GPE"]
        },
        "member_of": {
            "allowed_head": ["PERSON"],
            "allowed_tail": ["ORG"]
        },
        "affiliated_with": {
            "allowed_head": ["ORG"],
            "allowed_tail": ["GPE"]
        },
        "participated_in": {
            "allowed_head": ["ORG", "PERSON"],
            "allowed_tail": ["EVENT"] 
        },
        "occurred_at": {
            "allowed_head": ["EVENT"],
            "allowed_tail": ["LOC", "GPE", "FACILITY"]
        },
        "occurred_on": {
            "allowed_head": ["EVENT"],
            "allowed_tail": ["DATE"]
        },
        "leader_of": {
            "allowed_head": ["PERSON"],
            "allowed_tail": ["GPE", "ORG"]
        },
        "allied_with": {
            "allowed_head": ["GPE"],
            "allowed_tail": ["GPE"]
        },
        "no_relation": {}
    }
}

SCRAPE_HEADERS: typing.Dict[ str, str ] = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
}

SPACY_MODEL: str = "en_core_web_md"

STOP_WORDS: typing.Set[ str ] = set([
    "PRON.it",
    "PRON.that",
    "PRON.they",
    "PRON.those",
    "PRON.we",
    "PRON.which",
    "PRON.who",
])

TR_ALPHA: float = 0.85
TR_LOOKBACK: int = 3


######################################################################
## data validation classes

class TextChunk (LanceModel):
    uid: int
    url: str
    text: str = EMBED_FCN.SourceField()
    vector: Vector(EMBED_FCN.ndims()) = EMBED_FCN.VectorField(default = None)


@dataclass(order=False, frozen=False)
class Entity:
    loc: typing.Tuple[ int ]
    key: str
    text: str
    label: str
    chunk_id: int
    sent_id: int
    span: spacy.tokens.span.Span
    node: typing.Optional[ int ] = None


######################################################################
## collect unstructured data from specific web page sources

@task
def uni_scrubber (
    span: spacy.tokens.span.Span,
    ) -> str:
    """
    Cleans text by removing garbled Unicode and spurious punctuation.

    Part of the text pre-processing pipeline to ensure high-quality input
    for entity and relationship extraction.
    """

    text: str = span.text

    if type(text).__name__ != "str":
        print("not a string?", type(text), text)

    limpio: str = " ".join(map(lambda s: s.strip(), text.split("\n"))).strip()

    limpio = limpio.replace('“', '"').replace('”', '"')
    limpio = limpio.replace("‘", "'").replace("’", "'").replace("`", "'").replace("â", "'")
    limpio = limpio.replace("…", "...").replace("–", "-")

    limpio = str(unicodedata.normalize("NFKD", limpio).encode("ascii", "ignore").decode("utf-8"))

    return limpio

@task
def make_chunk (
    doc: spacy.tokens.doc.Doc,
    url: str,
    chunk_list: typing.List[ TextChunk ],
    chunk_id: int,
    ) -> int:
    """
    Splits a document into text chunks of a fixed size for efficient processing.

    Uses recommendations from the RAG (Retrieval-Augmented Generation) system 
    to optimize chunk size for embedding and storage.

    Args:
        doc: The input document to chunk.
        url: The source URL for reference.
        chunk_list: List to store the resulting chunks.
        chunk_id: Current chunk index.
        
    Returns:
        Updated chunk ID after processing.
    """

    chunks: typing.List[ str ] = []
    chunk_total: int = 0
    prev_line: str = ""

    for sent_id, sent in enumerate(doc.sents):
        line: str = uni_scrubber(sent)
        line_len: int = len(line)
    
        if (chunk_total + line_len) > CHUNK_SIZE:
            # emit the current chunk
            chunk_list.append(
                TextChunk(
                    uid = chunk_id,
                    url = url,
                    text = "\n".join(chunks),
                )
            )

            # start a new chunk
            chunks = [ prev_line, line ]
            chunk_total = len(prev_line) + line_len
            chunk_id += 1
        else:
            # append line to the current chunk
            chunks.append(line)
            chunk_total += line_len

        prev_line = line

    # emit the trailing chunk
    chunk_list.append(
        TextChunk(
            uid = chunk_id,
            url = url,
            text = "\n".join(chunks),
        )
    )

    return chunk_id + 1

@task
def scrape_html (
    scrape_nlp: spacy.Language,
    url: str,
    chunk_list: typing.List[ TextChunk ],
    chunk_id: int,
    ) -> int:
    """
    Fetches text from a webpage and performs chunking on the content.

    Combines HTML scraping with NLP-based chunking for streamlined data ingestion
    into the knowledge graph workflow.

    Args:
        scrape_nlp: spaCy language model for text processing.
        url: Web page URL to scrape.
        chunk_list: List to store text chunks.
        chunk_id: Current chunk index.
        
    Returns:
        Updated chunk ID after processing the webpage.
    """

    logger = get_run_logger()
    response: requests.Response = requests.get(
        url,
        headers = SCRAPE_HEADERS,
    )

    soup: BeautifulSoup = BeautifulSoup(
        response.text,
        features = "lxml",
    )

    scrape_doc: spacy.tokens.doc.Doc = scrape_nlp("\n".join([
        para.text.strip()
        for para in soup.findAll("p")
    ]))

    chunk_id = make_chunk(
        scrape_doc,
        url,
        chunk_list,
        chunk_id,
    )

    return chunk_id


######################################################################
## lexical graph construction

@task
def init_nlp (
    ) -> spacy.Language:
    """
    Initializes the NLP pipeline with spaCy, GLiNER, and GLiREL models.

    Sets up Named Entity Recognition (NER) and Relationship Extraction (RE)
    to identify domain-specific entities and their connections.

    Returns:
        Initialized spaCy language object.
    """

    # override specific Hugging Face error messages, since
    # `transformers` and `tokenizers` have noisy logging
    logging.disable(logging.ERROR)
    transformers.logging.set_verbosity_error()
    os.environ["TOKENIZERS_PARALLELISM"] = "0"

    # load models for `spaCy`, `GLiNER`, `GLiREL`
    # this may take several minutes when run the first time
    nlp: spacy.Language = spacy.load(SPACY_MODEL)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        nlp.add_pipe(
            "gliner_spacy",
            config = {
                "gliner_model": GLINER_MODEL,
                "labels": NER_LABELS,
                "chunk_size": CHUNK_SIZE,
                "style": "ent",
            },
        )
        
        nlp.add_pipe(
            "glirel",
            after = "ner",
        )

    return nlp

@task
def parse_text (
    nlp: spacy.Language,
    known_lemma: typing.List[ str ],
    lex_graph: nx.Graph,
    chunk: TextChunk,
    *,
    debug: bool = False,
    ) -> spacy.tokens.doc.Doc:
    """
    Parses text chunks to construct a lexical graph and extract entities.

    Combines spaCy parsing with TextRank-inspired co-occurrence algorithms to 
    create a graph representation of text.

    Args:
        nlp: Initialized NLP pipeline.
        known_lemma: List of lemmas encountered so far.
        lex_graph: Graph to store lexical relations.
        chunk: Text chunk to parse.
        debug: Enables debugging logs.
        
    Returns:
        Parsed spaCy document.
    """

    logger = get_run_logger()
    doc: spacy.tokens.doc.Doc = list(
        nlp.pipe(
            [( chunk.text, RE_LABELS )],
            as_tuples = True,
        )
    )[0][0]

    # scan the document tokens to add lemmas to _lexical graph_ using
    # a _textgraph_ approach called the _textrank_ algorithm
    for sent in doc.sents:
        node_seq: typing.List[ int ] = []

        if debug:
            logger.debug(sent)

        for tok in sent:
            text: str = tok.text.strip()
        
            if tok.pos_ in [ "NOUN", "PROPN" ]:
                key: str = tok.pos_ + "." + tok.lemma_.strip().lower()
                prev_known: bool = False
    
                if key not in known_lemma:
                    # create a new node
                    known_lemma.append(key)
                else:
                    # link to an existing node, adding weight
                    prev_known = True

                node_id: int = known_lemma.index(key)
                node_seq.append(node_id)

                if not lex_graph.has_node(node_id):
                    lex_graph.add_node(
                        node_id,
                        key = key,
                        kind = "Lemma",
                        pos = tok.pos_,
                        text = text,
                        chunk = chunk,
                        count = 1,
                    )

                elif prev_known:
                    node: dict = lex_graph.nodes[node_id]
                    node["count"] += 1

        # create the _textrank_ edges for the lexical graph,
        # which will get used for ranking, but discarded later
        if debug:
            logger.debug(node_seq)

        for hop in range(TR_LOOKBACK):
            for node_id, node in enumerate(node_seq[: -1 - hop]):            
                neighbor: int = node_seq[hop + node_id + 1]
    
                if not lex_graph.has_edge(node, neighbor):
                    lex_graph.add_edge(
                        node,
                        neighbor,
                        rel = "FOLLOWS_LEXICALLY",
                    )

    return doc

@task
def make_entity (
    span_decoder: typing.Dict[ tuple, Entity ],
    sent_map: typing.Dict[ spacy.tokens.span.Span, int ],
    span: spacy.tokens.span.Span,
    chunk: TextChunk,
    *,
    debug: bool = False,
    ) -> Entity:
    """
    Creates an `Entity` object from a recognized text span.

    Facilitates integration of identified entities into the knowledge graph
    as nodes for downstream analysis.

    Args:
        span_decoder: Decoder for span-to-entity mapping.
        sent_map: Sentence-to-entity mapping.
        span: Text span identified as an entity.
        chunk: Associated text chunk.
        debug: Enables debugging logs.
        
    Returns:
        Created `Entity` object.
    """

    logger = get_run_logger()
    key: str = " ".join([
        tok.pos_ + "." + tok.lemma_.strip().lower()
        for tok in span
    ])

    ent: Entity = Entity(
        ( span.start, span.end, ),
        key,
        span.text,
        span.label_,
        chunk.uid,
        sent_map[span.sent],
        span,
    )

    if ent.loc not in span_decoder:
        span_decoder[ent.loc] = ent

        if debug:
            logger.debug(ent)

    return ent

@task
def extract_entity (
    known_lemma: typing.List[ str ],
    lex_graph: nx.Graph,
    ent: Entity,
    *,
    debug: bool = False,
    ) -> None:
    """
    Links an entity into the lexical graph.

    Ensures that entities are represented as nodes with appropriate
    connections to lemmas or other entities.

    Args:
        known_lemma: List of previously known lemmas.
        lex_graph: Lexical graph for storing entities.
        ent: Entity to extract and link.
        debug: Enables debugging logs.
    """

    logger = get_run_logger()
    prev_known: bool = False

    if ent.key not in known_lemma:
        # add a new Entity node to the graph and link to its component Lemma nodes
        known_lemma.append(ent.key)
    else:
        # phrase for this entity has been previously seen in other documents
        prev_known = True

    node_id: int = known_lemma.index(ent.key)
    ent.node = node_id

    # hydrate a compound phrase in this doc's lexical graph
    if not lex_graph.has_node(node_id):
        lex_graph.add_node(
            node_id,
            key = ent.key,
            kind = "Entity",
            label = ent.label,
            pos = "NP",
            text = ent.text,
            chunk = ent.chunk_id,
            count = 1,
        )

        for tok in ent.span:
            tok_key: str = tok.pos_ + "." + tok.lemma_.strip().lower()

            if tok_key in known_lemma:
                tok_idx: int = known_lemma.index(tok_key)

                lex_graph.add_edge(
                    node_id,
                    tok_idx,
                    rel = "COMPOUND_ELEMENT_OF",
                )

    if prev_known:
        # promote a previous Lemma node to an Entity
        node: dict = lex_graph.nodes[node_id]
        node["kind"] = "Entity"
        node["chunk"] = ent.chunk_id
        node["count"] += 1

        # select the more specific label
        if "label" not in node or node["label"] == "NP":
            node["label"] = ent.label
    
    if debug:
        logger.debug(ent)

@task
def extract_relations (
    known_lemma: typing.List[ str ],
    lex_graph: nx.Graph,
    span_decoder: typing.Dict[ tuple, Entity ],
    sent_map: typing.Dict[ spacy.tokens.span.Span, int ],
    doc: spacy.tokens.doc.Doc,
    chunk: TextChunk,
    *,
    debug: bool = False,
    ) -> None:
    """
    Extracts relationships between entities using GLiREL.

    Adds inferred relationships as edges in the lexical graph, ensuring a
    robust representation of entity interactions.

    Args:
        known_lemma: List of previously known lemmas.
        lex_graph: Lexical graph for storing relationships.
        span_decoder: Decoder for span-to-entity mapping.
        sent_map: Sentence-to-entity mapping.
        doc: Parsed spaCy document.
        chunk: Associated text chunk.
        debug: Enables debugging logs.
    """

    relations: typing.List[ dict ] = sorted(
        doc._.relations,
        key = lambda item: item["score"],
        reverse = True,
    )

    for item in relations:
        src_loc: typing.Tuple[ int ] = tuple(item["head_pos"])
        dst_loc: typing.Tuple[ int ] = tuple(item["tail_pos"])
        redact_rel: bool = False

        if src_loc not in span_decoder:
            if debug:
                print("MISSING src entity:", item["head_text"], item["head_pos"])

            src_ent: Entity = make_entity(
                span_decoder,
                sent_map,
                doc[ item["head_pos"][0] : item["head_pos"][1] ],
                chunk,
                debug = debug,
            )

            if src_ent.key in STOP_WORDS:
                redact_rel = True
            else:
                extract_entity(
                    known_lemma,
                    lex_graph,
                    src_ent,
                    debug = debug
                )

        if dst_loc not in span_decoder:
            if debug:
                print("MISSING dst entity:", item["tail_text"], item["tail_pos"])

            dst_ent: Entity = make_entity(
                span_decoder,
                sent_map,
                doc[ item["tail_pos"][0] : item["tail_pos"][1] ],
                chunk,
                debug = debug,
            )

            if dst_ent.key in STOP_WORDS:
                redact_rel = True
            else:
                extract_entity(
                    known_lemma,
                    lex_graph,
                    dst_ent,
                    debug = debug
                )

        # link the connected nodes
        if not redact_rel:
            src_ent = span_decoder[src_loc]
            dst_ent = span_decoder[dst_loc]

            rel: str = item["label"].strip().replace(" ", "_").upper()
            prob: float = round(item["score"], 3)

            if debug:
                print(f"{src_ent.text} -> {rel} -> {dst_ent.text} | {prob}")

            lex_graph.add_edge(
                src_ent.node,
                dst_ent.node,
                rel = rel,
                prob = prob,
            )

######################################################################
## numerical utilities

@task
def calc_quantile_bins (
    num_rows: int,
    *,
    amplitude: int = 4,
    ) -> np.ndarray:
    """
    Calculate the bins to use for a quantile stripe,
    using [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)

        num_rows:
    number of rows in the target dataframe

        returns:
    calculated bins, as a `numpy.ndarray`
    """
    granularity = max(round(math.log(num_rows) * amplitude), 1)

    return np.linspace(
        0,
        1,
        num = granularity,
        endpoint = True,
    )

@task
def stripe_column (
    values: list,
    bins: int,
    ) -> np.ndarray:
    """
    Stripe a column in a dataframe, by interpolating quantiles into a set of discrete indexes.

        values:
    list of values to stripe

        bins:
    quantile bins; see [`calc_quantile_bins()`](#calc_quantile_bins-function)

        returns:
    the striped column values, as a `numpy.ndarray`
    """
    s = pd.Series(values)
    q = s.quantile(bins, interpolation = "nearest")

    try:
        stripe = np.digitize(values, q) - 1
        return stripe
    except ValueError as ex:
        # should never happen?
        print("ValueError:", str(ex), values, s, q, bins)
        raise

@task
def root_mean_square (
    values: typing.List[ float ]
    ) -> float:
    """
    Calculate the [*root mean square*](https://mathworld.wolfram.com/Root-Mean-Square.html)
    of the values in the given list.

        values:
    list of values to use in the RMS calculation

        returns:
    RMS metric as a float
    """
    s: float = sum(map(lambda x: float(x) ** 2.0, values))
    n: float = float(len(values))

    return math.sqrt(s / n)

######################################################################
## textrank algorithm for co-occurence and node ranking

@task
def connect_entities (
    lex_graph: nx.Graph,
    span_decoder: typing.Dict[ tuple, Entity ],
    ) -> None:
    """
    Connect entities which co-occur within the same sentence.
    """
    ent_map: typing.Dict[ int, typing.Set[ int ]] = defaultdict(set)

    for ent in span_decoder.values():
        if ent.node is not None:
            ent_map[ent.sent_id].add(ent.node)    

    for sent_id, nodes in ent_map.items():
        for pair in itertools.combinations(list(nodes), 2):
            if not lex_graph.has_edge(*pair):
                lex_graph.add_edge(
                    pair[0],
                    pair[1],
                    rel = "CO_OCCURS_WITH",
                    prob = 1.0,
                )

@task
def run_textrank (
    lex_graph: nx.Graph,
    ) -> pd.DataFrame:
    """
    Ranks entities in the lexical graph using a PageRank-inspired algorithm.

    Calculates centrality metrics to prioritize key entities for downstream tasks.

    Args:
        lex_graph: Lexical graph containing entities and relationships.
        
    Returns:
        DataFrame of ranked entities.
    """

    # build a dataframe of node ranks and counts
    df_rank: pd.DataFrame = pd.DataFrame.from_dict([
        {
            "node_id": node,
            "weight": rank,
            "count": lex_graph.nodes[node]["count"],
        }
        for node, rank in nx.pagerank(lex_graph, alpha = TR_ALPHA, weight = "count").items()
    ])

    # normalize by column and calculate quantiles
    df1: pd.DataFrame = df_rank[[ "count", "weight" ]].apply(lambda x: x / x.max(), axis = 0)
    bins: np.ndarray = calc_quantile_bins(len(df1.index))

    # stripe each columns
    df2: pd.DataFrame = pd.DataFrame([
        stripe_column(values, bins)
        for _, values in df1.items()
    ]).T

    # renormalize the ranks
    df_rank["rank"] = df2.apply(root_mean_square, axis=1)
    rank_col: np.ndarray = df_rank["rank"].to_numpy()
    rank_col /= sum(rank_col)
    df_rank["rank"] = rank_col

    # move the ranked weights back into the graph
    for _, row in df_rank.iterrows():
        node: int = row["node_id"]
        lex_graph.nodes[node]["rank"] = row["rank"]

    df: pd.DataFrame = pd.DataFrame([
        node_attr
        for node, node_attr in lex_graph.nodes(data = True)
        if node_attr["kind"] == "Entity"
    ]).sort_values(by = [ "rank" ], ascending = False)

    return df

######################################################################
## abstracting the semantic overlay out of the lexical graph

@task
def abstract_overlay (
    url: str,
    chunk_list: typing.List[ TextChunk ],
    lex_graph: nx.Graph,
    sem_overlay: nx.Graph,
    ) -> None:
    """
    Creates a semantic overlay by promoting entities and relationships from 
    the lexical graph to a higher-level representation.

    Connects entities to their source chunks, enabling context-aware knowledge graphs.

    Args:
        url: Source URL for the data.
        chunk_list: List of processed text chunks.
        lex_graph: Lexical graph to abstract.
        sem_overlay: Graph to store the semantic overlay.
    """

    kept_nodes: typing.Set[ int ] = set()
    skipped_rel: typing.Set[ str ] = set([ "FOLLOWS_LEXICALLY", "COMPOUND_ELEMENT_OF" ])

    chunk_nodes: typing.Dict[ int, str ] = {
        chunk.uid: f"chunk_{chunk.uid}"
        for chunk in chunk_list
    }

    for chunk_id, node_id in chunk_nodes.items():
        sem_overlay.add_node(
            node_id,
            kind = "Chunk",
            chunk = chunk_id,
            url = url,
        )

    for node_id, node_attr in lex_graph.nodes(data = True):
        if node_attr["kind"] == "Entity":
            kept_nodes.add(node_id)                
            count: int = node_attr["count"]

            if not sem_overlay.has_node(node_id):
                sem_overlay.add_node(
                    node_id,
                    kind = "Entity",
                    key = node_attr["key"],
                    text = node_attr["text"],
                    label = node_attr["label"],
                    count = count,
                )
            else:
                sem_overlay.nodes[node_id]["count"] += count

            sem_overlay.add_edge(
                node_id,
                chunk_nodes[node_attr["chunk"]],
                rel = "WITHIN",
                weight = node_attr["rank"],
            )

    for src_id, dst_id, edge_attr in lex_graph.edges(data = True):
        if src_id in kept_nodes and dst_id in kept_nodes:
            rel: str = edge_attr["rel"]
            prob: float = 1.0

            if "prob" in edge_attr:
                prob = edge_attr["prob"]

            if rel not in skipped_rel:
                if not sem_overlay.has_edge(src_id, dst_id):
                    sem_overlay.add_edge(
                        src_id,
                        dst_id,
                        rel = rel,
                        prob = prob,
                    )
                else:
                    sem_overlay[src_id][dst_id]["prob"] = max(
                        prob,
                        sem_overlay.edges[(src_id, dst_id)]["prob"],
                    )

######################################################################
## graph visualization

def gen_pyvis (
    graph: nx.Graph,
    html_file: str,
    *,
    num_docs: int = 1,
    notebook: bool = False,
    ) -> None:
    """
    Use `pyvis` to provide an interactive visualization of the graph layers.
    """
    pv_net: pyvis.network.Network = pyvis.network.Network(
        height = "900px",
        width = "100%",
        notebook = notebook,
        cdn_resources = "remote",
    )

    for node_id, node_attr in graph.nodes(data = True):
        if node_attr.get("kind") == "Entity":
            color: str = "hsla(65, 46%, 58%, 0.80)"
            size: int = round(20 * math.log(1.0 + math.sqrt(float(node_attr.get("count"))) / num_docs))
            label: str = node_attr.get("text")
            title: str = node_attr.get("key")
        else:
            color = "hsla(306, 45%, 57%, 0.95)"
            size = 5
            label = node_id
            title = node_attr.get("url")

        pv_net.add_node(
            node_id,
            label = label,
            title = title,
            color = color,
            size = size,
        )

    for src_node, dst_node, edge_attr in graph.edges(data = True):
        pv_net.add_edge(
            src_node,
            dst_node,
            title = edge_attr.get("rel"),
        )

        pv_net.toggle_physics(True)
        pv_net.show_buttons(filter_ = [ "physics" ])
        pv_net.save_graph(html_file)

@flow(name="construct_kg_parent", log_prints=True)
def construct_kg (
    url_list: typing.List[ str ],
    chunk_table: lancedb.table.LanceTable,
    sem_overlay: nx.Graph,
    w2v_file: pathlib.Path,
    *,
    debug: bool = True,
    ) -> None:
    """
    Orchestrates the construction of a knowledge graph from unstructured data.

    Integrates scraping, NLP processing, lexical graph creation, and visualization
    into a cohesive pipeline for knowledge graph generation.

    Args:
        url_list: List of URLs to process.
        chunk_table: LanceDB table to store chunks and embeddings.
        sem_overlay: Semantic overlay graph.
        w2v_file: File path to save Word2Vec embeddings.
        debug: Enables debugging logs.
    """

    logger = get_run_logger()
    # define the global data structures which must be reset for each
    # run, not on each chunk iteration
    nlp: spacy.Language = init_nlp()
    known_lemma: typing.List[ str ] = []
    w2v_vectors: list = []

    # iterate through the URL list, scraping text and building chunks
    chunk_id: int = 0
    scrape_nlp: spacy.Language = spacy.load(SPACY_MODEL)

    for url in url_list:
        lex_graph: nx.Graph = nx.Graph()
        chunk_list: typing.List[ TextChunk ] = []

        chunk_id = scrape_html(
            scrape_nlp,
            url,
            chunk_list,
            chunk_id,
        )

        chunk_table.add(chunk_list)

        # parse each chunk to build a lexical graph per source URL
        for chunk in chunk_list:
            span_decoder: typing.Dict[ tuple, Entity ] = {}

            doc: spacy.tokens.doc.Doc = parse_text(
                nlp,
                known_lemma,
                lex_graph,
                chunk,
                debug = debug,
            )

            # keep track of sentence numbers per chunk, to use later
            # for entity co-occurrence links
            sent_map: typing.Dict[ spacy.tokens.span.Span, int ] = {}

            for sent_id, sent in enumerate(doc.sents):
                sent_map[sent] = sent_id

            # classify the recognized spans within this chunk as
            # potential entities

            # NB: if we'd run [_entity resolution_]
            # see: <https://neo4j.com/developer-blog/entity-resolved-knowledge-graphs/>
            # previously from _structured_ or _semi-structured_ data sources to
            # generate a "backbone" for the knowledge graph, then we could use
            # contextualized _surface forms_ perform _entity linking_ on the
            # entities extracted here from _unstructured_ data

            for span in doc.ents:
                make_entity(
                    span_decoder,
                    sent_map,
                    span,
                    chunk,
                    debug = debug,
                )

            for span in doc.noun_chunks:
                make_entity(
                    span_decoder,
                    sent_map,
                    span,
                    chunk,
                    debug = debug,
                )

            # overlay the recognized entity spans atop the base layer
            # constructed by _textgraph_ analysis of the `spaCy` parse trees
            for ent in span_decoder.values():
                if ent.key not in STOP_WORDS:
                    extract_entity(
                        known_lemma,
                        lex_graph,
                        ent,
                        debug = debug,
                    )

            # extract relations for co-occurring entity pairs
            extract_relations(
                known_lemma,
                lex_graph,
                span_decoder,
                sent_map,
                doc,
                chunk,
                debug = debug,
            )

            # connect entities which co-occur within the same sentence
            connect_entities(
                lex_graph,
                span_decoder,
            )

            # build the vector input for entity embeddings
            w2v_map: typing.Dict[ int, typing.Set[ str ]] = defaultdict(set)

            for ent in span_decoder.values():
                if ent.node is not None:
                    w2v_map[ent.sent_id].add(ent.key)

            for sent_id, ents in w2v_map.items():
                vec: list = list(ents)
                vec.insert(0, str(sent_id))
                w2v_vectors.append(vec)

        # apply _textrank_ to the graph (in the url/doc iteration)
        # then report the top-ranked extracted entities
        df: pd.DataFrame = run_textrank(
            lex_graph,
        )

        #logger.info(url, df.head(20))

        # abstract a semantic overlay from the lexical graph
        # and persist this in the resulting KG
        abstract_overlay(
            url,
            chunk_list,
            lex_graph,
            sem_overlay,
        )

        print("nodes", len(sem_overlay.nodes), "edges", len(sem_overlay.edges))


    # train the entity embedding model
    w2v_max: int = max([
        len(vec) - 1
        for vec in w2v_vectors
    ])

    w2v_model: gensim.models.Word2Vec = gensim.models.Word2Vec(
        w2v_vectors,
        min_count = 2,
        window = w2v_max,
    )

    w2v_model.save(str(w2v_file))

    # serialize the resulting KG
    with pathlib.Path("../data/processed/graphrag_demo.json").open("w", encoding = "utf-8") as fp:
        fp.write(
            json.dumps(
                nx.node_link_data(sem_overlay, edges="edges"),
                indent = 2,
                sort_keys = True,
            )
        )

    # Path to save the GraphML file
    graphml_path = pathlib.Path("../data/processed/graphrag_demo.graphml")

    # Serialize the NetworkX graph to GraphML format using a with statement
    with graphml_path.open("wb") as fp:  # Open in binary write mode
        nx.write_graphml(sem_overlay, fp)

    gen_pyvis(
        sem_overlay,
        "../data/processed/graphrag_demo.html",
        num_docs = len(url_list),
    )

######################################################################
## main entry point

if __name__ == "__main__":

    url_list: typing.List[ str ] = [
        "https://raw.githubusercontent.com/donbr/kg_rememberall/refs/heads/main/references/winston_churchill_we_shall_fight_speech_june_1940.txt",
    ]

    vect_db: lancedb.db.LanceDBConnection = lancedb.connect(LANCEDB_URI)

    chunk_table: lancedb.table.LanceTable = vect_db.create_table(
        "chunk",
        schema = TextChunk,
        mode = "overwrite",
    )

    sem_overlay: nx.Graph = nx.Graph()

    construct_kg(
        url_list,
        chunk_table,
        sem_overlay,
        pathlib.Path("../models/entity.w2v"),
        debug = False,  # True
    )
