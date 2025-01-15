# Combined Context for LLM

Source Directory: ../data/raw/GLiREL
Generated On: 2025-01-14 08:50:31

## SOURCE:  https://github.com/jackboyla/GLiREL

- refer to README for citation details.

## Directory Summary

* .png: 1 files
* .py: 24 files
* .jpg: 1 files
* .txt: 2 files
* .toml: 1 files
* .md: 2 files
* No extension: 1 files
* .yaml: 7 files

## Table of Contents

- [Combined Context for LLM](#combined-context-for-llm)
  - [SOURCE:  https://github.com/jackboyla/GLiREL](#source--httpsgithubcomjackboylaglirel)
  - [Directory Summary](#directory-summary)
  - [Table of Contents](#table-of-contents)
  - [File: image.png](#file-imagepng)
  - [File: quickstart\_demo\_spacy.py](#file-quickstart_demo_spacypy)
  - [File: eval\_with\_gpt.py](#file-eval_with_gptpy)
  - [File: demo.jpg](#file-demojpg)
  - [File: quickstart\_demo.py](#file-quickstart_demopy)
  - [File: requirements.txt](#file-requirementstxt)
  - [File: pyproject.toml](#file-pyprojecttoml)
  - [File: requirements-dev.txt](#file-requirements-devtxt)
  - [File: README.md](#file-readmemd)
  - [Usage](#usage)
    - [Expected Output](#expected-output)
  - [Constrain labels](#constrain-labels)
  - [Usage with spaCy](#usage-with-spacy)
    - [Expected Output](#expected-output-1)
  - [Example training data](#example-training-data)
  - [License](#license)
  - [Citation](#citation)
  - [File: train.py](#file-trainpy)
  - [File: eval.py](#file-evalpy)
  - [File: RELEASE.md](#file-releasemd)
  - [Releases](#releases)
    - [Step 1: Adjust the version of your package](#step-1-adjust-the-version-of-your-package)
    - [Step 2: (Optional) Make sure all tests pass](#step-2-optional-make-sure-all-tests-pass)
    - [Step 3: Add a tag for your release](#step-3-add-a-tag-for-your-release)
    - [Step 4: (Optional) Prepare the release notes](#step-4-optional-prepare-the-release-notes)
    - [Step 5: Create the wheels for your release](#step-5-create-the-wheels-for-your-release)
    - [Step 6: Upload your package on PyPI test](#step-6-upload-your-package-on-pypi-test)
    - [Step 7: Publish on PyPI](#step-7-publish-on-pypi)
    - [Step 8: (Optional) Publish your release notes](#step-8-optional-publish-your-release-notes)
    - [Step 9: Bump the dev version on the main branch](#step-9-bump-the-dev-version-on-the-main-branch)
  - [File: glirel/__init__.py](#file-glirelinitpy)
  - [File: glirel/model.py](#file-glirelmodelpy)
  - [File: glirel/test\_spacy\_integration.py](#file-glireltest_spacy_integrationpy)
  - [File: glirel/spacy\_integration.py](#file-glirelspacy_integrationpy)
  - [File: glirel/modules/evaluator.py](#file-glirelmodulesevaluatorpy)
  - [File: glirel/modules/token\_rep.py](#file-glirelmodulestoken_reppy)
  - [File: glirel/modules/loss\_functions.py](#file-glirelmodulesloss_functionspy)
  - [File: glirel/modules/span\_rep.py](#file-glirelmodulesspan_reppy)
  - [File: glirel/modules/custom\_tokenizers.py](#file-glirelmodulescustom_tokenizerspy)
  - [File: glirel/modules/utils.py](#file-glirelmodulesutilspy)
  - [File: glirel/modules/run\_evaluation.py](#file-glirelmodulesrun_evaluationpy)
  - [File: glirel/modules/base.py](#file-glirelmodulesbasepy)
  - [File: glirel/modules/\___init__.py](#file-glirelmodules_initpy)
  - [File: glirel/modules/layers.py](#file-glirelmoduleslayerspy)
  - [File: glirel/modules/rel\_rep.py](#file-glirelmodulesrel_reppy)
  - [File: glirel/modules/data\_proc.py](#file-glirelmodulesdata_procpy)
  - [File: glirel/modules/test\_rel\_rep.py](#file-glirelmodulestest_rel_reppy)
  - [File: examples/finetune.py](#file-examplesfinetunepy)
  - [File: configs/config\_nyt.yaml](#file-configsconfig_nytyaml)
  - [File: configs/config\_finetuning.yaml](#file-configsconfig_finetuningyaml)
  - [File: configs/config\_redocred.yaml](#file-configsconfig_redocredyaml)
  - [File: configs/config\_zero\_rel.yaml](#file-configsconfig_zero_relyaml)
  - [File: configs/config\_docred.yaml](#file-configsconfig_docredyaml)
  - [File: configs/config\_few\_rel.yaml](#file-configsconfig_few_relyaml)
  - [File: configs/config\_wiki\_zsl.yaml](#file-configsconfig_wiki_zslyaml)

## File: image.png

<a name='file-image.png'></a>
*Description*: No specific description available.

*This file is binary and cannot be displayed as text.*
## File: quickstart_demo_spacy.py

<a name='file-quickstart_demo_spacy.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# In[1]:


import spacy
import glirel

# Load a blank spaCy model or an existing one
nlp = spacy.load('en_core_web_sm')

# Add the GLiREL component to the pipeline
nlp.add_pipe("glirel", after="ner")

# Now you can use the pipeline with the GLiREL component
text = "Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in April 1976. The company is headquartered in Cupertino, California."

labels = {"glirel_labels": {
    'co-founder': {"allowed_head": ["PERSON"], "allowed_tail": ["ORG"]}, 
    'country of origin': {"allowed_head": ["PERSON", "ORG"], "allowed_tail": ["LOC", "GPE"]}, 
    'licensed to broadcast to': {"allowed_head": ["ORG"]},  
    'no relation': {},  
    'parent': {"allowed_head": ["PERSON"], "allowed_tail": ["PERSON"]}, 
    'followed by': {"allowed_head": ["PERSON", "ORG"], "allowed_tail": ["PERSON", "ORG"]},  
    'located in or next to body of water': {"allowed_head": ["LOC", "GPE", "FAC"], "allowed_tail": ["LOC", "GPE"]},  
    'spouse': {"allowed_head": ["PERSON"], "allowed_tail": ["PERSON"]},  
    'child': {"allowed_head": ["PERSON"], "allowed_tail": ["PERSON"]},  
    'founder': {"allowed_head": ["PERSON"], "allowed_tail": ["ORG"]},  
    'headquartered in': {"allowed_head": ["ORG"], "allowed_tail": ["LOC", "GPE", "FAC"]},  
    'acquired by': {"allowed_head": ["ORG"], "allowed_tail": ["ORG", "PERSON"]},  
    'subsidiary of': {"allowed_head": ["ORG"], "allowed_tail": ["ORG", "PERSON"]}, 
    }
}

docs = list( nlp.pipe([(text, labels)], as_tuples=True) )
relations = docs[0][0]._.relations

print('Number of relations:', len(relations))

sorted_data_desc = sorted(relations, key=lambda x: x['score'], reverse=True)
print("\nDescending Order by Score:")
for item in sorted_data_desc:
    print(f"{item['head_text']} --> {item['label']} --> {item['tail_text']} | score: {item['score']}")


# In[ ]:





```

## File: eval_with_gpt.py

<a name='file-eval_with_gpt.py'></a>
*Description*: This is a Python script.

```python
import argparse
import os

import torch
from tqdm import tqdm
from transformers import get_cosine_schedule_with_warmup, get_cosine_with_hard_restarts_schedule_with_warmup

# from model_nested import NerFilteredSemiCRF
from glirel import GLiREL
from glirel.modules.run_evaluation import sample_train_data
from glirel.model import load_config_as_namespace
from glirel.modules.evaluator import greedy_search, RelEvaluator
from datetime import datetime
import json
import logging
import random
import shutil
import wandb
from functools import partial
from sklearn.model_selection import train_test_split
import time
import gc
import asyncio
import instructor
import openai
from enum import Enum
from pydantic import BaseModel, field_validator, Field
from asyncio import run as aiorun
from typing import List, Dict, Literal
import textwrap


logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])

'''

python eval_with_gpt.py --model gpt-4o \
    --eval-data data/few_rel_all.jsonl \
    --num-unseen-rel-types 5 \
    --seed 42

python eval_with_gpt.py \
    --predictions-file logs/gpt-wiki_zsl/wiki_zsl-2024-10-07__08-52-44/eval-predictions-gpt-4o-mini.jsonl \
        --eval-data data/wiki_zsl_all.jsonl
    
'''

client = instructor.from_openai(openai.AsyncOpenAI())


def create_parser():
    parser = argparse.ArgumentParser(description="Zero-shot Relation Extraction")
    parser.add_argument("--model", type=str, default=None, help="LLM model name")
    parser.add_argument("--eval-data", type=str, default=None, help="Path to evaluation data")
    parser.add_argument("--dataset-name", type=str, default=None, help="Name under which to save the logs")
    parser.add_argument("--num-unseen-rel-types", type=int, default=15, help="Number of unseen relation types for zero-shot learning")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for splitting data")
    parser.add_argument("--skip-splitting", action='store_true', help="Skip splitting data eval set")
    parser.add_argument("--predictions-file", type=str, default=None, help="output predictions path if it already exists")
    return parser


def get_unique_relations(data):
    unique_rel_types = []
    for item in data:
        for r in item['relations']:
            unique_rel_types.append(r["relation_text"])
    unique_rel_types = list(set(unique_rel_types))
    return unique_rel_types


def split_data_by_relation_type(data, num_unseen_rel_types, seed=None):
    """
    Attempts to split a dataset into training and testing sets based on relation types,
    aiming to have a specified number of unique relation types exclusively in the test set
    to simulate a zero-shot learning scenario. The function shuffles and splits the relation
    types, allocating the first chunk as unseen relation types for testing and the rest for training.
    
    It iteratively adjusts the number of unseen relation types if the initial split does not achieve
    the desired number of unique test relation types, retrying with an incremented number until it succeeds
    or the number reaches twice the original request, resetting as needed.

    Notes:
        - This function relies heavily on the assumption that sufficient relation diversity exists
          to meet the zero-shot criteria. If not, the test set may not end up with the intended
          number of unique unseen relation types.
        - The function can potentially skip a significant number of items that contain both train and
          test relation types, leading to data wastage.
        - The iterative process to adjust unseen relation types may lead to computational inefficiency,
          especially for large datasets with diverse relations.
    """

    unique_relations = get_unique_relations(data)
    correct_num_unseen_relations_achieved = False
    original_num_unseen_rel_types = num_unseen_rel_types

    logger.info(f"Running dataset splitting...")
    start = time.time()
    count = 0
    if seed is None:
        seed = random.randint(0, 1000)
    while correct_num_unseen_relations_achieved is False:
        random.seed(seed)
        random.shuffle(unique_relations)
        test_relation_types = set(unique_relations[ : num_unseen_rel_types ])
        train_relation_types = set(unique_relations[ num_unseen_rel_types : ])
        
        train_data = []
        test_data = []
        skipped_items = []
        
        # Splitting data based on relation types
        for item in data:
            relation_types = {r["relation_text"] for r in item['relations']}
            if relation_types.issubset(test_relation_types):
                test_data.append(item)
            elif relation_types.issubset(train_relation_types):
                train_data.append(item)
            else:
                # Entries that contain both train and test relation types are currently skipped
                skipped_items.append(item)
        
        # if we have the right number of eval relations, break
        if len(get_unique_relations(test_data)) == original_num_unseen_rel_types:
            correct_num_unseen_relations_achieved = True
        else:
            # bump the number of unseen relations by 1 to cast a wider net
            # if the bump gets too big, reset it
            num_unseen_rel_types = num_unseen_rel_types + 1 if (num_unseen_rel_types <  original_num_unseen_rel_types*2) else num_unseen_rel_types
            seed = random.randint(0, 1000)

        count += 1
        if count % 50 == 0:
            logger.info(f"Attempt {count} | Seed {seed}")

    if len(skipped_items) > 0:
        logger.info(f"Skipped items: {len(skipped_items)} because they have __BOTH__ train and test relation types")
    
    logger.info(f"Split on seed {seed}")
    logger.info(f"Splitting took {time.time() - start} seconds")
    return train_data, test_data
    
def dirty_split_data_by_relation_type(data, num_unseen_rel_types, max_test_size):
    '''
    This function does not care if the interesection of train and test relation types is empty.
    Used for custom datasets to avoid having a large number of eval classes (causes OOM), 
    and I do not mind if the eval set has some train classes.
    '''
    logger.info("Dirty splitting data...")

    unique_relations = get_unique_relations(data)
    correct_num_unseen_relations_achieved = False
    original_num_unseen_rel_types = num_unseen_rel_types


    while not correct_num_unseen_relations_achieved:
        seed = random.randint(0, 1000)
        random.seed(seed)
        random.shuffle(unique_relations)
        test_relation_types = set(unique_relations[ : num_unseen_rel_types ])
        
        train_data = []
        test_data = []

        # Splitting data based on relation types
        for item in data:
            relation_types = {r["relation_text"] for r in item['relations']}
            if len(test_data) < max_test_size and any([rel in test_relation_types for rel in relation_types]):
                test_data.append(item)
            else:
                train_data.append(item)

        # if we have the right number of eval relations, break
        if len(get_unique_relations(test_data)) == original_num_unseen_rel_types or len(test_data) >= max_test_size: 
            correct_num_unseen_relations_achieved = True
        else:
            # bump the number of unseen relations by 1 to cast a wider net
            # if the bump gets too big, reset it
            num_unseen_rel_types = num_unseen_rel_types + 1 if (num_unseen_rel_types <  original_num_unseen_rel_types*2) else num_unseen_rel_types


    return train_data, test_data


def eval_with_llm(model, log_dir, eval_rel_types, eval_data, predictions_file=None):

    async def async_eval_with_llm(eval_data, eval_rel_types, model, output_predictions):

        logger.info(f"🚀 Evaluating with LLM... 🚀")
        logger.info("Number of examples: ", len(eval_data))

        # eval_data = eval_data[:30]

        UNIQUE_LABELS = set(eval_rel_types)
        UNIQUE_LABELS.add("NO_RELATION")
        UNIQUE_LABELS = list(UNIQUE_LABELS)
        logger.info(f"UNIQUE LABELS: {UNIQUE_LABELS}")


        # use of Enum idea : https://stackoverflow.com/a/74335189
        class AnnotatedRelation(BaseModel):
            '''
            Classify the relationship between the HEAD and TAIL entities in the text,
            marked with [HEAD] and [TAIL] tokens respectively.
            Only use the relation labels provided to classify the relationship.
            If no relation exists, return 'NO_RELATION'
            '''
            head_entity: str
            tail_entity: str
            labels: List[str] = Enum("Labels", {l: l for l in UNIQUE_LABELS}, type=str)
            relation: List[labels] = Field(..., description="The relation between the head and tail entities. Before giving your answer, think carefully about this in the context of the given text.")

            @field_validator("relation")
            @classmethod
            def validate_relation(cls, relation: List[str]):
                if len(relation) > 1:
                    relation = [relation[0]]
                if 'NO_RELATION' in relation and len(relation) > 1:
                    raise ValueError("If 'NO_RELATION' is present, it should be the only label")
                elif any([label not in UNIQUE_LABELS for label in relation]):
                    raise ValueError(f"Invalid label found in relation: {relation}")
                return relation


        async def extract(message: Dict, model: str, output_predictions_path: str, text: str, relation: Dict):
            annotation = await client.chat.completions.create(
                model=model,
                messages=[
                    message,
                ],
                response_model=AnnotatedRelation,
                max_retries=3,
            )

            with open(output_predictions_path, "a+") as f:
                out = [text, relation, annotation.model_dump()['relation']]
                f.write(json.dumps(out) + "\n")
            
            return annotation

        async def batch_extract(messages: List[dict], model: str, output_predictions_path: str, texts: List[str], relations: List[Dict]) -> List["AnnotatedRelation"]:
            tasks = [
                extract(message, model, output_predictions_path, text, relation) for text, message, relation in zip(texts, messages, relations)
            ]
            results = await asyncio.gather(*tasks)
            return results


        prompt = textwrap.dedent(
        """
        Classify the relationship(s) between the HEAD and TAIL entities in the following text.
        Only use the relation labels provided to classify the relationship.
        If no relation exists, return ['NO_RELATION'].

        Text: {text}

        HEAD: {head}

        TAIL: {tail}

        Relation labels: {labels}
        """
        )
        messages = []
        text2messasge = {}
        for item in eval_data:
            for rel in item['relations']:
                head = rel['head']['mention']
                tail = rel['tail']['mention']
                text = " ".join(item['tokenized_text'])
                message = {
                    "role": "user", 
                    "content": prompt.format(text=text, head=head, tail=tail, labels=UNIQUE_LABELS)
                }
                messages.append(
                    {
                        "message": message,
                        "text": text,
                        'relation': rel,
                    }
                )
                if text in text2messasge:
                    text2messasge[text].append([messages[-1], rel['relation_text']])
                else:
                    text2messasge[text] = [[messages[-1], rel['relation_text']]]

        logger.info(f"Number of messages for {len(eval_data)} examples: {len(messages)}")
        batch_size = 100
        logger.info(f"🚀 Annotating {len(messages)} examples... 🚀")
        for batch in tqdm(range(0, len(messages), batch_size)):
            batch = messages[batch : batch+batch_size]
            batch_messages = [b['message'] for b in batch]
            batch_texts = [b['text'] for b in batch]
            batch_relations = [b['relation'] for b in batch]
            assert len(batch_messages) == len(batch_texts) == len(batch_relations)
            batch_messages = await batch_extract(
                batch_messages, 
                model=model, 
                output_predictions_path=output_predictions,
                texts=batch_texts,
                relations=batch_relations
            )

        logger.info(f"Annotation written to {output_predictions}")
        return
    
    if predictions_file is None:
        output_predictions = f"{log_dir}/eval-predictions-{model}.jsonl"
        asyncio.run(async_eval_with_llm(eval_data, eval_rel_types, model, output_predictions))
    else:
        logger.info(f"Predictions file already exists. Skipping annotation")
        output_predictions = predictions_file

    with open(output_predictions, "r") as f:
        predictions = [json.loads(line) for line in f]

    text2rel = {}
    for d in predictions:
        if d[0] not in text2rel:
            text2rel[d[0]] = [d[1]]
        else:
            text2rel[d[0]].append(d[1])
    
    gt_two_rels = [t for t,v in text2rel.items() if len(v) > 1]
    print(f"Texts with more than 2 relations: {gt_two_rels}")

    text2preds = {}
    text2trues = {}
    for idx, p in enumerate(predictions):

        if p[0] not in text2trues:
            text2trues[p[0]] = []
        text2trues[p[0]].append(p[1])

        if p[0] not in text2preds:
            text2preds[p[0]] = []
        if p[-1] in [['NO_RELATION'], []]:
            continue
        rel = {
            'head_text': p[1]['head']['mention'],
            'tail_text': p[1]['tail']['mention'],
            'head' : {'position': p[1]['head']['position']},
            'tail' : {'position': p[1]['tail']['position']},
            'relation_text': p[-1][0],
            'score': 1.0,
        }


        text2preds[p[0]].append(rel)


    preds = list(text2preds.values())
    all_trues = list(text2trues.values())
    for p, true, in zip(preds, all_trues):
            print(p, "-->", true)
    evaluator = RelEvaluator(all_trues, preds)
    out, metric_dict = evaluator.evaluate()
    logger.info(f"Metrics: {metric_dict}")


def main(args):

    if args.eval_data is not None:
        eval_data = args.eval_data

    if args.dataset_name is None:
        if 'wiki_zsl' in args.eval_data:
            dataset_name = 'wiki_zsl'
        elif 'redocred' in args.eval_data:
            dataset_name = 'redocred'
        elif 'fewrel' in args.eval_data or 'few_rel' in args.eval_data:
            dataset_name = 'fewrel'
        else:
            raise ValueError(f"Could not find dataset name from arg: {args.eval_data}. Please provide dataset name in --dataset-name")
    else:
        dataset_name = args.dataset_name

    # set up logging
    current_time = datetime.now().strftime("%Y-%m-%d__%H-%M-%S")
    log_dir = f'logs/gpt-{dataset_name}/{dataset_name}-{current_time}'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = "eval.log"
    log_file_path = os.path.join(log_dir, log_file)
    if os.path.exists(log_file_path):
        os.remove(log_file_path)
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info("🚀 Relation extraction evlauation started")
    logger.info(f"Evaluating on file {eval_data}")


    if isinstance(eval_data, str):
        eval_data_list = [eval_data]

    eval_data = []
    for eval_subset in eval_data_list:
        if eval_subset.endswith('.jsonl'):
            with open(eval_subset, 'r') as f:
                eval_subset = [json.loads(line) for line in f]
        elif eval_subset.endswith('.json'):
            with open(eval_subset, 'r') as f:
                eval_subset = json.load(f)
        else:
            raise ValueError(f"Invalid data format: {eval_data}. Must be .jsonl or .json")
        eval_data.extend(eval_subset)

    if args.skip_splitting is False:
        _, eval_data = split_data_by_relation_type(eval_data, args.num_unseen_rel_types, seed=args.seed)


    eval_rel_types = get_unique_relations(eval_data)
    if eval_data is not None:
        logger.info(f"Num Eval relation types: {len(eval_rel_types)}")
        logger.info(f"Number of eval samples: {len(eval_data)}")

    if len(eval_rel_types) != args.num_unseen_rel_types:
        logger.info(f"Num eval types not set. Will take them on a batch by batch bases")
        eval_rel_types = None

    eval_with_llm(
        args.model, 
        log_dir, 
        eval_rel_types=eval_rel_types, 
        eval_data=eval_data,
        predictions_file=args.predictions_file
    )


if __name__ == "__main__":
    # parse args
    parser = create_parser()
    args = parser.parse_args()

    main(args)

```

## File: demo.jpg

<a name='file-demo.jpg'></a>
*Description*: No specific description available.

*This file is binary and cannot be displayed as text.*
## File: quickstart_demo.py

<a name='file-quickstart_demo.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding: utf-8

# # 🚞 Zero-shot RE Training

# In[1]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# In[2]:


# # if you're running this in a colab notebook, you can run this cell to install the necessary dependencies
# pip install glirel
# !python -m spacy download en_core_web_sm


# In[3]:


from glirel import GLiREL

save_path = 'logs/redocred/redocred-2024-09-17__17-53-16/model_42900'
model = GLiREL.from_pretrained(save_path, map_location='cpu')
# model = GLiREL.from_pretrained('jackboyla/glirel_beta')


# # Inference
# 
# To infer, the model needs `tokens`, `NER`, and `zero shot labels`.

# ### Eval data

# In[4]:


import json
with open('./data/few_rel_all.jsonl', 'r') as f:
    data = [json.loads(line) for line in f]

i = 0

tokens = data[i]['tokenized_text']
ner = data[i]['ner']
labels = list(set([r['relation_text'] for r in data[i]['relations']]))
print(tokens)
print()
print(ner)
print(labels)


# In[5]:


labels = ['country of origin', 'licensed to broadcast to', 'father', 'followed by'] + labels
print(labels)


# In[6]:


relations = model.predict_relations(tokens, labels, threshold=0.0, ner=ner)

print('Number of relations:', len(relations))  # num entity pairs (both directions) * num classes.... provided they're over the threshold

sorted_data_desc = sorted(relations, key=lambda x: x['score'], reverse=True)
print("\nDescending Order by Score:")
for item in sorted_data_desc:
    print(item)


# ### Real-world example
# 
# Constrain the entity types that can associated with a relationship.
# e.g:
# 
# `co-founder` can only have a head `PERSON` entity and a tail `ORG` entity.

# In[7]:


# Real-world example
import spacy
from glirel.modules.utils import constrain_relations_by_entity_type

nlp = spacy.load('en_core_web_sm')


text = "Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in April 1976. The company is headquartered in Cupertino, California."

# text = "Jack Dorsey's father, Tim Dorsey, is a licensed pilot. Jack met his wife Sarah Paulson in New York in 2003. They have one son, Edward."

labels = {"glirel_labels": {
    'co-founder': {"allowed_head": ["PERSON"], "allowed_tail": ["ORG"]}, 
    'country of origin': {"allowed_head": ["PERSON", "ORG"], "allowed_tail": ["LOC", "GPE"]}, 
    'licensed to broadcast to': {"allowed_head": ["ORG"]},  
    'no relation': {},  
    'parent': {"allowed_head": ["PERSON"], "allowed_tail": ["PERSON"]}, 
    'followed by': {"allowed_head": ["PERSON", "ORG"], "allowed_tail": ["PERSON", "ORG"]},  
    'located in or next to body of water': {"allowed_head": ["LOC", "GPE", "FAC"], "allowed_tail": ["LOC", "GPE"]},  
    'spouse': {"allowed_head": ["PERSON"], "allowed_tail": ["PERSON"]},  
    'child': {"allowed_head": ["PERSON"], "allowed_tail": ["PERSON"]},  
    'founder': {"allowed_head": ["PERSON"], "allowed_tail": ["ORG"]},  
    'founded on date': {"allowed_head": ["ORG"], "allowed_tail": ["DATE"]},
    'headquartered in': {"allowed_head": ["ORG"], "allowed_tail": ["LOC", "GPE", "FAC"]},  
    'acquired by': {"allowed_head": ["ORG"], "allowed_tail": ["ORG", "PERSON"]},  
    'subsidiary of': {"allowed_head": ["ORG"], "allowed_tail": ["ORG", "PERSON"]}, 
    }
}


def predict_and_show(text, labels):
    doc = nlp(text)
    print(f"Text: {text}")

    tokens = [token.text for token in doc]

    # NOTE: the end index should be inclusive
    ner = [[ent.start, (ent.end - 1), ent.label_, ent.text] for ent in doc.ents]
    print(f"Entities detected: {ner}")

    labels_and_constraints = None
    if isinstance(labels, dict):
        labels = labels["glirel_labels"]
        labels_and_constraints = labels
        labels = list(labels.keys())

    relations = model.predict_relations(tokens, labels, threshold=0.0, ner=ner, top_k=1)

    if isinstance(labels_and_constraints, dict):
        print('Constraining relations by entity type')
        relations = constrain_relations_by_entity_type(doc.ents, labels_and_constraints, relations)

    print('Number of relations:', len(relations))

    sorted_data_desc = sorted(relations, key=lambda x: x['score'], reverse=True)
    print("\nDescending Order by Score:")
    for item in sorted_data_desc:
        print(f"{item['head_text']} --> {item['label']} --> {item['tail_text']} | score: {item['score']}")

predict_and_show(text, labels)


# A simple list of relation types can also be passed, although this generally results in noisier results.

# In[8]:


text = "Jack knows Gill. They live in the same house in London. They are not related."
labels = ['family relation', 'knows', 'lives with', 'loves', 'licensed to broadcast to', 'father', 'followed by', 'no relation', 'lives in',]
predict_and_show(text, labels)


# In[10]:


# import huggingface_hub
# import os

# huggingface_hub.login(os.environ['HF_TOKEN'])

# model.save_pretrained(
#     './release_model/glirel_beta', 
#     push_to_hub=True, 
#     repo_id='jackboyla/glirel_beta'
# )


# ### Co-reference Resolution

# In[27]:


import json
with open('data/redocred_test.jsonl', 'r') as f:
    data = [json.loads(line) for line in f] 

examples = data[:5]
batch_tokenized_text = [example['tokenized_text'] for example in examples]
batch_ner = [example['ner'] for example in examples]
print(batch_tokenized_text[0])
print()
print(batch_ner[0])
print()

batch_labels = [list(set([r['relation_text'] for r in example['relations']])) for example in examples]
batch_labels[0]


# In[37]:


model.base_config.fixed_relation_types = False
model = model.to('cpu')
relations = model.batch_predict_relations(batch_tokenized_text, batch_labels, threshold=0.01, ner=batch_ner, top_k=1)
relations[0]


# In[34]:


from glirel.modules.utils import get_coreference_clusters, aggregate_cluster_relations

clusters_batch, entity_to_cluster_idx_batch = get_coreference_clusters(relations)
print("Clusters:", clusters_batch[0])
print()
cluster_relations_batch = aggregate_cluster_relations(entity_to_cluster_idx_batch, relations)
cluster_relations_batch[0]


# In[36]:


for cluster, cluster_relations_list, tokenized_text in zip(clusters_batch, cluster_relations_batch, batch_tokenized_text):
    for cluster_relations in cluster_relations_list:
        print()
        cluster_h_idx = cluster_relations['h_idx']
        cluster_t_idx = cluster_relations['t_idx']
        head_cluster = [tokenized_text[s:e] for s, e in cluster[cluster_h_idx]]
        print(f"Head Cluster: {head_cluster}")
        print(f"Relation: {cluster_relations['r']}")
        tail_cluster = [tokenized_text[s:e] for s, e in cluster[cluster_t_idx]]
        print(f"Tail Cluster: {tail_cluster}")


# ### Coreference in the Wild
# Give a real news story

# In[28]:


# Real-world example
import spacy
from glirel.modules.utils import constrain_relations_by_entity_type
from glirel.modules.utils import get_coreference_clusters, aggregate_cluster_relations

from fastcoref import FCoref
fcoref_model = FCoref(device='cpu', enable_progress_bar=False)

nlp = spacy.load('en_core_web_sm')


text = """Polish city urged to evacuate as floods batter central Europe
A flooded area in Nysa, Poland
Image source,Reuters
Image caption,
A flooded area in Nysa, Poland

Laura Gozzi, Nick Thorpe, Adam Easton and Rob Cameron
BBC News
Reporting from
London, Budapest, Warsaw and Prague
Published
16 September 2024
The mayor of a Polish city has asked all 44,000 residents to evacuate, as widespread flooding continues to batter central Europe.

Nysa mayor Kordian Kolbiarz asked people to head for higher ground, citing the risk of an embankment breaching and releasing a cascade of water into the town from a nearby lake.

The death toll from the floods that hit over the weekend rose to at least 16 on Monday, with seven confirmed fatalities in Romania. Casualties were also recorded in Austria, the Czech Republic and Poland.

Budapest said it would close roads near the river Danube which runs through the Hungarian capital, citing the risk of flooding later this week.

“Please evacuate your belongings, yourselves, your loved ones. It is worth getting to the top floor of the building immediately, because the wave may be several metres high. This means that the whole town will be flooded,” Nysa Mayor Kolbiarz wrote.

Polish Prime Minister Donald Tusk said one billion zloty (£197m) would be allocated for flood victims in the country, adding that Poland would also apply for EU relief funds. His government has also declared a state of natural disaster.

Although conditions have stabilised in some places, others are bracing themselves for more disruption and danger from the floods, sparked by Storm Boris.

In Slovakia, the overflowing of the Danube River caused flooding in the Old Town area of the capital, Bratislava, with local media reporting that water levels exceeded 9m (30ft) and were expected to rise further.

A dog being lifted by Polish rescuers
Image source,Getty Images
Image caption,
Polish rescuers and soldiers evacuated local residents and their pets in the village of Rudawa, southern Poland

Watch on BBC iPlayer (UK Only)
From Above - Storm Boris
Attribution
iPlayer
Hungary is bracing itself for floods in the coming days. Warnings are in force along 500km (310 miles) of the Danube.

The river is rising by about a metre every 24 hours, with Budapest's mayor offering residents a million sandbags to protect against floodwaters.

Some tram lines will not operate, while roads along the river will be closed in the Hungarian capital from Monday evening. Trains between Budapest and Vienna have also been cancelled.

Prime Minister Viktor Orban said on X that he had postponed all his international obligations "due to the extreme weather conditions and the ongoing floods in Hungary".

The highest rainfall totals have been in the Czech Republic. In the north-eastern town of Jesenik, 473mm (19in) of rain has fallen since Thursday morning - five times the average monthly rainfall.

The Czech fire service delivered bottles of drinking water to stranded villages, where people were told not to drink water from their taps or their wells as it is likely heavily contaminated.

In the Austrian town of St Polten, more rain has fallen in four days than in the whole of the wettest autumn on record, in 1950.

Chancellor Karl Nehammer said the armed forces had been deployed to offer assistance to storm-hit regions. Austria's Climate Ministry said €300m (£253m) in recovery funds would be made available.

Most parties paused campaigning for the federal elections due in less than two weeks, on 29 September.

Villages and town were submerged in eastern Romania. Emil Dragomir, mayor of Slobozia Conachi, told media that the flooding had had a devastating impact.

"If you were here, you would cry instantly, because people are desperate, their whole lives' work is gone, there were people who were left with just the clothes they had on," he said.

Thousands of people have been evacuted in Poland, including the personnel and patients of a hospital in the town of Nysa. Roads have been badly disrupted and train traffic was suspended in many parts of the country.

On Monday morning, the mayor of Paczków in south-west Poland appealed to residents to evacuate after water began overflowing in a nearby reservoir, endangering the town.


Media caption,
Airborne rescues as Europe hit by floods

In other parts of Poland, however, water levels are now falling, according to local officials.

The mayor of Klodzko city, Michal Piszko, told Polish media the water had receded and the indications were the worst was now over.

Video footage from Monday morning showed that city centre streets which were inundated on Sunday were now water-free, although the footage also revealed the extent of damage done to the buildings.

Where will Storm Boris go next?
More rain is expected throughout Monday and Tuesday in Austria, the Czech Republic and south-east Germany, where another 100mm could fall.

While it may still take days for the flood waters to subside, the weather will improve in central Europe from mid-week with much drier conditions.

Storm Boris will, however, now move further south into Italy, where it will reintensify and bring heavy rain. The Emilia-Romagna region is set to be worst hit, with 100-150mm of rain falling.

The record rainfall seen in central Europe has been caused by a number of factors, including climate change.

Different weather elements came together to create a “perfect storm” in which very cold air from the Arctic met warm air from the Mediterranean.

A pattern of atmospheric pressure also meant that Storm Boris was stuck in one place for a long time.

Scientists say that a warmer atmosphere holds more moisture, leading to more intense rainfall. Warmer oceans also lead to more evaporation, feeding storm systems.

For every 1C rise in the global average temperature, the atmosphere is able to hold about 7% more moisture, external."""


labels = [
    "SELF",
    # Positive relation labels
    "mayor responsible for evacuation",
    "flood causes evacuation",
    "country affected by floods",
    "storm responsible for floods",
    "government allocates funds",
    "river causes flood",
    "mayor issues warning",
    "rescue teams assist residents",
    "prime minister declares disaster",
    "city experiences flood damage",
    "rescue of people and animals",
    "flooding disrupts transport",
    "climate change causes extreme weather",
    "scientists explain weather patterns",
    
    # Negative relation labels
    "mayor responsible for storm",
    "train causes flood",
    "flooding creates more jobs",
    "rescue teams cause damage",
    "election delayed by storm"
]




def predict_and_show(text, labels, coreference=False):
    doc = nlp(text)
    # print(f"Text: {text}")

    tokens = [token.text for token in doc]

    # NOTE: the end index should be inclusive
    ner = [[ent.start, (ent.end - 1), ent.label_, ent.text] for ent in doc.ents]
    # print(f"Entities detected: {ner}")

    labels_and_constraints = None
    if isinstance(labels, dict):
        labels = labels["glirel_labels"]
        labels_and_constraints = labels
        labels = list(labels.keys())

    relations = model.batch_predict_relations([tokens], [labels], threshold=0.01, ner=[ner], top_k=1)

    if isinstance(labels_and_constraints, dict):
        print('Constraining relations by entity type')
        relations = constrain_relations_by_entity_type(doc.ents, labels_and_constraints, relations)



    mention_char_spans = [(m.start_char, m.end_char) for m in doc.ents]
    if len(mention_char_spans) == 0:
        raise ValueError("No entities detected in the text. Please provide entities for coreference resolution.")
    else:
        output = fcoref_model.predict(
            texts=doc.text, custom_mentions=mention_char_spans
        )
    char_idx2tok_idx = {(ent.start_char, ent.end_char): (ent.start, ent.end) for ent in doc.ents}

    entity_to_cluster_idx_batch = {}
    fcoref_output = output.get_clusters(as_strings=False)
    # map positions to cluster id
    for cluster_id, cluster in enumerate(fcoref_output):
        for mention in cluster:
            token_pos = char_idx2tok_idx[mention]
            entity_to_cluster_idx_batch[(token_pos[0], token_pos[1])] = cluster_id
    all_indices = [idx for cluster in fcoref_output for idx in cluster]
    # add singletons
    cluster_id = len(fcoref_output)
    for k, token_pos in char_idx2tok_idx.items():
        if k not in all_indices:
            entity_to_cluster_idx_batch[(token_pos[0], token_pos[1])] = cluster_id
            fcoref_output.append([k])
            cluster_id += 1
    # sort by start idx of keys
    entity_to_cluster_idx_batch = dict(sorted(entity_to_cluster_idx_batch.items(), key=lambda x: x[0][0]))
    
    clusters_batch = [
        [[(char_idx2tok_idx[(s, e)][0], char_idx2tok_idx[(s, e)][1]) for s, e in cluster] for cluster in fcoref_output]
    ]


    # clusters_batch, entity_to_cluster_idx_batch = get_coreference_clusters(relations)
    print()
    cluster_relations_batch = aggregate_cluster_relations(entity_to_cluster_idx_batch, relations)
    cluster_relations_batch[0]

    batch_tokenized_text = [tokens]
    
    for cluster, cluster_relations_list, tokenized_text in zip(clusters_batch, cluster_relations_batch, batch_tokenized_text):
        print(f"len of (cluster, cluster_relations_list, tokenized_text): {len(cluster), len(cluster_relations_list), len(tokenized_text)}")
        for cluster_relations in cluster_relations_list:
            print()
            cluster_h_idx = cluster_relations['h_idx']
            cluster_t_idx = cluster_relations['t_idx']
            head_cluster = [tokenized_text[s:e] for s, e in cluster[cluster_h_idx]]
            print(f"Head Cluster: {head_cluster}")
            print(f"Relation: {cluster_relations['r']}")
            print(f"on cluster idx: {cluster_h_idx}")             
            tail_cluster = [tokenized_text[s:e] for s, e in cluster[cluster_t_idx]]
            print(f"Tail Cluster: {tail_cluster}")



predict_and_show(text, labels, coreference=True)


# In[ ]:





```

## File: requirements.txt

<a name='file-requirements.txt'></a>
*Description*: This text file contains general information.

```plaintext
torch
transformers
huggingface_hub
flair
seqeval
tqdm
wandb
scipy==1.10.1
loguru
```

## File: pyproject.toml

<a name='file-pyproject.toml'></a>
*Description*: No specific description available.

```plaintext
[build-system]
requires = ["setuptools>=61.0.0"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
include = ["glirel", "glirel.*"]

[tool.setuptools.dynamic]
version = {attr = "glirel.__version__"}

[project]
name = "glirel"
description = "Generalist model for Relation Extraction (Extract any relation types from texts)"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "Apache-2.0"}
keywords = [
    "named-entity-recognition",
    "ner",
    "data-science",
    "natural-language-processing",
    "artificial-intelligence",
    "nlp",
    "machine-learning",
    "transformers"
]
authors = [
    {name = "Jack Boylan"},
    {name = "Urchade Zaratiana"},
    {name = "Nadi Tomeh"},
    {name = "Pierre Holat"},
    {name = "Thierry Charnois"},
]
maintainers = [
    {name = "Jack Boylan"},
]
dependencies = [
    "torch",
    "transformers",
    "huggingface_hub",
    "flair",
    "seqeval",
    "tqdm",
    "datasets",
]
dynamic = ["version"]

[project.urls]
Homepage = "https://github.com/jackboyla/GLiREL"
```

## File: requirements-dev.txt

<a name='file-requirements-dev.txt'></a>
*Description*: This text file contains general information.

```plaintext
spacy
datasets
ipdb
pytest
build
twine
```

## File: README.md

<a name='file-README.md'></a>
*Description*: No specific description available.

```plaintext
# GLiREL : Generalist and Lightweight model for Zero-Shot Relation Extraction

GLiREL is a Relation Extraction model capable of classifying unseen relations given the entities within a text. This builds upon the excelent work done by Urchade Zaratiana, Nadi Tomeh, Pierre Holat, Thierry Charnois on the [GLiNER](https://github.com/urchade/GLiNER) library which enables efficient zero-shot Named Entity Recognition.


<p align="center">
    <a href="https://pypi.org/project/glirel/" target="_blank">
        <img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
        <img alt="Version" src="https://img.shields.io/pypi/v/glirel?style=for-the-badge&color=3670A0">
    </a>
</p>

<p align="center">
    <a href="https://arxiv.org/abs/2501.03172">📄 GLiREL Paper</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="https://arxiv.org/abs/2311.08526">📄 GLiNER Paper</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="https://huggingface.co/spaces/jackboyla/GLiREL">🤗 Demo</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="https://huggingface.co/collections/jackboyla/glirel-6766b213a4c1fa8c4e982322">🤗 Available models</a>
</p>

---
# Installation

```bash
pip install glirel
```

## Usage
Once you've downloaded the GLiREL library, you can import the `GLiREL` class. You can then load this model using `GLiREL.from_pretrained` and predict entities with `predict_relations`.

```python
from glirel import GLiREL
import spacy

model = GLiREL.from_pretrained("jackboyla/glirel-large-v0")

nlp = spacy.load('en_core_web_sm')

text = 'Derren Nesbitt had a history of being cast in "Doctor Who", having played villainous warlord Tegana in the 1964 First Doctor serial "Marco Polo".'
doc = nlp(text)
tokens = [token.text for token in doc]

labels = ['country of origin', 'licensed to broadcast to', 'father', 'followed by', 'characters']

ner = [[26, 27, 'PERSON', 'Marco Polo'], [22, 23, 'Q2989412', 'First Doctor']] # 'type' is not used -- it can be any string!

relations = model.predict_relations(tokens, labels, threshold=0.0, ner=ner, top_k=1)

print('Number of relations:', len(relations))

sorted_data_desc = sorted(relations, key=lambda x: x['score'], reverse=True)
print("\nDescending Order by Score:")
for item in sorted_data_desc:
    print(f"{item['head_text']} --> {item['label']} --> {item['tail_text']} | score: {item['score']}")
```

### Expected Output

```
Number of relations: 2

Descending Order by Score:
{'head_pos': [26, 28], 'tail_pos': [22, 24], 'head_text': ['Marco', 'Polo'], 'tail_text': ['First', 'Doctor'], 'label': 'characters', 'score': 0.9923334121704102}
{'head_pos': [22, 24], 'tail_pos': [26, 28], 'head_text': ['First', 'Doctor'], 'tail_text': ['Marco', 'Polo'], 'label': 'characters', 'score': 0.9915636777877808}
```

## Constrain labels
In practice, we usually want to define the types of entities that can exist as a head and/or tail of a relationship. This is already implemented in GLiREL:

```python
labels = {"glirel_labels": {
    'co-founder': {"allowed_head": ["PERSON"], "allowed_tail": ["ORG"]}, 
    'no relation': {},  # head and tail can be any entity type 
    'country of origin': {"allowed_head": ["PERSON", "ORG"], "allowed_tail": ["LOC", "GPE"]}, 
    'parent': {"allowed_head": ["PERSON"], "allowed_tail": ["PERSON"]}, 
    'located in or next to body of water': {"allowed_head": ["LOC", "GPE", "FAC"], "allowed_tail": ["LOC", "GPE"]},  
    'spouse': {"allowed_head": ["PERSON"], "allowed_tail": ["PERSON"]},  
    'child': {"allowed_head": ["PERSON"], "allowed_tail": ["PERSON"]},  
    'founder': {"allowed_head": ["PERSON"], "allowed_tail": ["ORG"]},  
    'founded on date': {"allowed_head": ["ORG"], "allowed_tail": ["DATE"]},
    'headquartered in': {"allowed_head": ["ORG"], "allowed_tail": ["LOC", "GPE", "FAC"]},  
    'acquired by': {"allowed_head": ["ORG"], "allowed_tail": ["ORG", "PERSON"]},  
    'subsidiary of': {"allowed_head": ["ORG"], "allowed_tail": ["ORG", "PERSON"]}, 
    }
}
```

## Usage with spaCy

You can also load GliREL into a regular spaCy NLP pipeline. Here's an example using an English pipeline.

```python
import spacy
import glirel

# Load a blank spaCy model or an existing one
nlp = spacy.load('en_core_web_sm')

# Add the GLiREL component to the pipeline
nlp.add_pipe("glirel", after="ner")

# Now you can use the pipeline with the GLiREL component
text = "Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in April 1976. The company is headquartered in Cupertino, California."

labels = {"glirel_labels": {
    'co-founder': {"allowed_head": ["PERSON"], "allowed_tail": ["ORG"]}, 
    'country of origin': {"allowed_head": ["PERSON", "ORG"], "allowed_tail": ["LOC", "GPE"]}, 
    'licensed to broadcast to': {"allowed_head": ["ORG"]},  
    'no relation': {},  
    'parent': {"allowed_head": ["PERSON"], "allowed_tail": ["PERSON"]}, 
    'followed by': {"allowed_head": ["PERSON", "ORG"], "allowed_tail": ["PERSON", "ORG"]},  
    'located in or next to body of water': {"allowed_head": ["LOC", "GPE", "FAC"], "allowed_tail": ["LOC", "GPE"]},  
    'spouse': {"allowed_head": ["PERSON"], "allowed_tail": ["PERSON"]},  
    'child': {"allowed_head": ["PERSON"], "allowed_tail": ["PERSON"]},  
    'founder': {"allowed_head": ["PERSON"], "allowed_tail": ["ORG"]},  
    'headquartered in': {"allowed_head": ["ORG"], "allowed_tail": ["LOC", "GPE", "FAC"]},  
    'acquired by': {"allowed_head": ["ORG"], "allowed_tail": ["ORG", "PERSON"]},  
    'subsidiary of': {"allowed_head": ["ORG"], "allowed_tail": ["ORG", "PERSON"]}, 
    }
}

# Add the labels to the pipeline at inference time
docs = list( nlp.pipe([(text, labels)], as_tuples=True) )
relations = docs[0][0]._.relations

print('Number of relations:', len(relations))

sorted_data_desc = sorted(relations, key=lambda x: x['score'], reverse=True)
print("\nDescending Order by Score:")
for item in sorted_data_desc:
    print(f"{item['head_text']} --> {item['label']} --> {item['tail_text']} | score: {item['score']}")

```

### Expected Output

```
Number of relations: 5

Descending Order by Score:
['Apple', 'Inc.'] --> headquartered in --> ['California'] | score: 0.9854260683059692
['Apple', 'Inc.'] --> headquartered in --> ['Cupertino'] | score: 0.9569844603538513
['Steve', 'Wozniak'] --> co-founder --> ['Apple', 'Inc.'] | score: 0.09025496244430542
['Steve', 'Jobs'] --> co-founder --> ['Apple', 'Inc.'] | score: 0.08805803954601288
['Ronald', 'Wayne'] --> co-founder --> ['Apple', 'Inc.'] | score: 0.07996643334627151
```


## Example training data

NOTE that the entity indices are inclusive i.e `"Binsey"` is `[7, 7]`. This differs from spaCy where the end index is exclusive (in this case spaCy would set the indices to `[7, 8]`)

JSONL file:
```json
{
  "ner": [
    [7, 7, "Q4914513", "Binsey"], 
    [11, 12, "Q19686", "River Thames"]
  ], 
  "relations": [
    {
      "head": {"mention": "Binsey", "position": [7, 7], "type": "LOC"}, # 'type' is not used -- it can be any string!
      "tail": {"mention": "River Thames", "position": [11, 12], "type": "Q19686"}, 
      "relation_text": "located in or next to body of water"
    }
  ], 
  "tokenized_text": ["The", "race", "took", "place", "between", "Godstow", "and", "Binsey", "along", "the", "Upper", "River", "Thames", "."]
},
{
  "ner": [
    [9, 10, "Q4386693", "Legislative Assembly"], 
    [1, 3, "Q1848835", "Parliament of Victoria"]
  ], 
  "relations": [
    {
      "head": {"mention": "Legislative Assembly", "position": [9, 10], "type": "Q4386693"}, 
      "tail": {"mention": "Parliament of Victoria", "position": [1, 3], "type": "Q1848835"}, 
      "relation_text": "part of"
    }
  ], 
  "tokenized_text": ["The", "Parliament", "of", "Victoria", "consists", "of", "the", "lower", "house", "Legislative", "Assembly", ",", "the", "upper", "house", "Legislative", "Council", "and", "the", "Queen", "of", "Australia", "."]
}
```

## License

[GLiREL](https://github.com/jackboyla/GLiREL) by [Jack Boylan](https://github.com/jackboyla) is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1).

<a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer">
    <img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="CC Logo" style="height: 20px; margin-right: 5px; vertical-align: text-bottom;">
    <img src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt="BY Logo" style="height: 20px; margin-right: 5px; vertical-align: text-bottom;">
    <img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt="NC Logo" style="height: 20px; margin-right: 5px; vertical-align: text-bottom;">
    <img src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt="SA Logo" style="height: 20px; margin-right: 5px; vertical-align: text-bottom;">
</a>


## Citation
If you use code or ideas from this project, please cite:
```
@misc{boylan2025glirelgeneralistmodel,
      title={GLiREL -- Generalist Model for Zero-Shot Relation Extraction},
      author={Jack Boylan and Chris Hokamp and Demian Gholipour Ghalandari},
      year={2025},
      eprint={2501.03172},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.03172},
}
```


```

## File: Makefile

<a name='file-Makefile'></a>
*Description*: No specific description available.

```plaintext

test:
	pytest

dev:
	pip install -e .
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	python -m spacy download en_core_web_sm

docred_download:
	gdown --folder 1c5-0YwnoJx8NS6CV2f-NoTHR__BdkNqw
	mv DocRED/train_distant.json data/re-docred/train_distant.json

```

## File: train.py

<a name='file-train.py'></a>
*Description*: This is a Python script.

```python
import argparse
import os

import torch
import numpy as np
from tqdm import tqdm
from transformers import get_cosine_schedule_with_warmup, get_cosine_with_hard_restarts_schedule_with_warmup
from transformers.trainer import (
    is_sagemaker_mp_enabled,
    get_parameter_names,
    ALL_LAYERNORM_LAYERS,
)

# from model_nested import NerFilteredSemiCRF
from glirel import GLiREL
from glirel.modules.run_evaluation import sample_train_data
from glirel.model import load_config_as_namespace
from datetime import datetime
import json
import logging
import random
import shutil
import wandb
from functools import partial
from sklearn.model_selection import train_test_split
import time
import gc
import sys
sys.path.append('data/re-docred')
from run_evaluation import run_evaluation
from redocred_experiment_params import REDOCRED_EXP_SWEEP_CONFIG


logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])

'''

python train.py --config configs/config_wiki_zsl.yaml --wandb_sweep


python train.py --config configs/config_few_rel.yaml

CUDA_VISIBLE_DEVICES="0" python train.py --config configs/config_few_rel.yaml --wandb_sweep --sweep_method grid --experiment


'''

# If doing hyperparameter sweeping, define sweep config here
HP_SWEEP_CONFIG = {
    "metric": {"goal": "maximize", "name": "eval_f1_macro"},
    "parameters": {
        "scorer": {"values": ["dot", "dot_norm", "dot_thresh", "concat_proj"]},
        # "num_train_rel_types": {"values": [15, 20, 25, 30, 35, 40]},
        # "num_unseen_rel_types": {"values": [15]},
        # "random_drop": {"values": [True, False]},
        "lr_encoder": {"values": [1e-5, 5e-5, 1e-4, 5e-4, 1e-3, 5e-3]},
        "lr_others": {"values": [1e-4, 5e-4, 1e-3, 5e-3]},
        'num_layers_freeze': {"values": [None, 2, 4, 7, 10]},
        "refine_prompt": {"values": [True, False]},
        "refine_relation": {"values": [True, False]},
        "dropout": {"values": [0.3, 0.4, 0.5]},
        "loss_func": {"values": ["binary_cross_entropy_loss", "focal_loss"]},
        "alpha": {"values": [0.3, 0.5, 0.75]},  # focal loss only
        "gamma": {"values": [1, 3, 5]},         # focal loss only
        # "model_name": {"values": ["microsoft/deberta-v3-large", "microsoft/deberta-v3-small"]},
    },
}

EXP_SWEEP_CONFIG = {
    "metric": {"goal": "maximize", "name": "eval_f1_macro"},
    "parameters": {
        'seed': {"values": [11222333, 457365, 495538, 94757, 4756273, 385563]}, 
        # "refine_prompt": {"values": [False, True]},
        # "refine_relation": {"values": [False, True]},
        # "span_marker_mode": {"values": ["markerv1", "markerv2"]},
        # "add_entity_markers": {"values": [False, True]},
        # "label_embed_strategy": {"values": ["label"]},
        # "random_drop": {"values": [False]},
        "num_unseen_rel_types": {"values": [ 10 ]},
        # "subtoken_pooling": {"values": ["mean", "first_last"]},   # "mean", "first_last", "first", "last"  # https://flairnlp.github.io/docs/tutorial-embeddings/transformer-embeddings#pooling-operation
        "prev_path": {"values": ["logs/zero_rel/zero_rel-2024-10-06__21-28-09/saved_at/model_70000" ]},  # 
    },
}


def create_parser():
    parser = argparse.ArgumentParser(description="Zero-shot Relation Extraction")
    parser.add_argument("--config", type=str, default="config.yaml", help="Path to config file")
    parser.add_argument('--log_dir', type=str, default=None, help='Path to the log directory')
    parser.add_argument("--wandb_log", action="store_true", help="Activate wandb logging")
    parser.add_argument("--wandb_sweep", action="store_true", help="Activate wandb hyperparameter sweep")
    parser.add_argument("--sweep_id", type=str, default=None, help="WandB Sweep ID")
    parser.add_argument("--sweep_method", type=str, default="grid", help="Sweep method (grid, random, bayes)")
    parser.add_argument("--skip_splitting", action="store_true", help="Skip dataset splitting into train and eval sets")
    parser.add_argument("--experiment", action="store_true", help="Run an experiment")
    return parser

def flush_memory():
    gc.collect()
    torch.cuda.empty_cache()

def get_unique_relations(data):
    unique_rel_types = []
    for item in data:
        for r in item['relations']:
            unique_rel_types.append(r["relation_text"])
    unique_rel_types = list(set(unique_rel_types))
    return unique_rel_types



def split_data_by_relation_type(data, num_unseen_rel_types, seed=None):
    """
    Attempts to split a dataset into training and testing sets based on relation types,
    aiming to have a specified number of unique relation types exclusively in the test set
    to simulate a zero-shot learning scenario. The function shuffles and splits the relation
    types, allocating the first chunk as unseen relation types for testing and the rest for training.
    
    It iteratively adjusts the number of unseen relation types if the initial split does not achieve
    the desired number of unique test relation types, retrying with an incremented number until it succeeds
    or the number reaches twice the original request, resetting as needed.

    Notes:
        - This function relies heavily on the assumption that sufficient relation diversity exists
          to meet the zero-shot criteria. If not, the test set may not end up with the intended
          number of unique unseen relation types.
        - The function can potentially skip a significant number of items that contain both train and
          test relation types, leading to data wastage.
        - The iterative process to adjust unseen relation types may lead to computational inefficiency,
          especially for large datasets with diverse relations.
    """

    unique_relations = get_unique_relations(data)
    correct_num_unseen_relations_achieved = False
    original_num_unseen_rel_types = num_unseen_rel_types

    logger.info(f"Running dataset splitting...")
    start = time.time()
    count = 0
    if seed is None:
        seed = random.randint(0, 1000)
    while correct_num_unseen_relations_achieved is False:
        random.seed(seed)
        random.shuffle(unique_relations)
        test_relation_types = set(unique_relations[ : num_unseen_rel_types ])
        train_relation_types = set(unique_relations[ num_unseen_rel_types : ])
        
        train_data = []
        test_data = []
        skipped_items = []
        
        # Splitting data based on relation types
        for item in data:
            relation_types = {r["relation_text"] for r in item['relations']}
            if relation_types.issubset(test_relation_types):
                test_data.append(item)
            elif relation_types.issubset(train_relation_types):
                train_data.append(item)
            else:
                # Entries that contain both train and test relation types are currently skipped
                skipped_items.append(item)
        
        # if we have the right number of eval relations, break
        if len(get_unique_relations(test_data)) == original_num_unseen_rel_types:
            correct_num_unseen_relations_achieved = True
        else:
            # bump the number of unseen relations by 1 to cast a wider net
            # if the bump gets too big, reset it
            num_unseen_rel_types = num_unseen_rel_types + 1 if (num_unseen_rel_types <  original_num_unseen_rel_types*2) else num_unseen_rel_types
            seed = random.randint(0, 1000)

        count += 1
        if count % 50 == 0:
            logger.info(f"Attempt {count} | Seed {seed}")

    if len(skipped_items) > 0:
        logger.info(f"Skipped items: {len(skipped_items)} because they have __BOTH__ train and test relation types")
    
    logger.info(f"Split on seed {seed}")
    logger.info(f"Splitting took {time.time() - start} seconds")
    return train_data, test_data

    
def dirty_split_data_by_relation_type(data, num_unseen_rel_types, max_test_size):
    '''
    This function does not care if the interesection of train and test relation types is empty.
    Used for custom datasets to avoid having a large number of eval classes (causes OOM), 
    and I do not mind if the eval set has some train classes.
    '''
    logger.info("Dirty splitting data...")

    unique_relations = get_unique_relations(data)
    correct_num_unseen_relations_achieved = False
    original_num_unseen_rel_types = num_unseen_rel_types


    while not correct_num_unseen_relations_achieved:
        seed = random.randint(0, 1000)
        random.seed(seed)
        random.shuffle(unique_relations)
        test_relation_types = set(unique_relations[ : num_unseen_rel_types ])
        
        train_data = []
        test_data = []

        # Splitting data based on relation types
        for item in data:
            relation_types = {r["relation_text"] for r in item['relations']}
            if len(test_data) < max_test_size and any([rel in test_relation_types for rel in relation_types]):
                test_data.append(item)
            else:
                train_data.append(item)

        # if we have the right number of eval relations, break
        if len(get_unique_relations(test_data)) == original_num_unseen_rel_types or len(test_data) >= max_test_size: 
            correct_num_unseen_relations_achieved = True
        else:
            # bump the number of unseen relations by 1 to cast a wider net
            # if the bump gets too big, reset it
            num_unseen_rel_types = num_unseen_rel_types + 1 if (num_unseen_rel_types <  original_num_unseen_rel_types*2) else num_unseen_rel_types


    return train_data, test_data


def freeze_n_layers(model, N):
    """
    Freezes or unfreezes the first n layers of the model.
    See DeBERTa model specs here: https://github.com/microsoft/DeBERTa?tab=readme-ov-file#pre-trained-models

    Args:
        model: Assumes model has a DeBERTa model under `model.token_rep_layer`
        n (int): Number of layers to freeze/unfreeze.
        freeze (bool): If True, freeze the layers; if False, unfreeze them.
    """
    # Ensure N is within the valid range
    total_layers = len(model.token_rep_layer.bert_layer.model.encoder.layer)
    if N < 0 or N > total_layers:
        raise ValueError(f"N must be between 0 and total layers ({total_layers}), got {N}")

    # Iterate over the first n layers
    for layer in model.token_rep_layer.bert_layer.model.encoder.layer[:N]:
        for param in layer.parameters():
            param.requires_grad = False

    logger.info(f"Freezing the first {N} layers of the model")
    return model


class EarlyStoppingException(Exception):
    pass


class EarlyStopping:
    def __init__(self, patience, delta, max_saves):
        """
        Args:
            patience (int): How long to wait after last time validation metric improved.
            verbose (bool): If True, prints a message for each validation metric improvement.
            delta (float): Minimum change in the monitored metric to qualify as an improvement.
            max_saves (int): Maximum number of models to save.
        """
        self.patience = patience
        self.delta = delta
        self.max_saves = max_saves

        self.saved_models = []
        self.counter = 0
        self.best_score = None
        self.early_stop = False
        self.best_metric = -np.Inf

    def __call__(self, metric, model, save_path) -> None:
        score = metric

        if self.best_score is None:
            self.best_score = score
            self.save_checkpoint(score, model, save_path)
        elif score < self.best_score + self.delta:
            self.counter += 1
            logger.info(f"Validation metric did not improve by delta ({self.delta}): ({self.best_score:.6f} --> {score:.6f}).")
            logger.info(f'EarlyStopping counter: {self.counter} out of {self.patience}')
            if self.counter >= self.patience:
                self.early_stop = True
                logger.info(f'Early stopping at step {self.counter}')
                raise EarlyStoppingException
        else:
            logger.info(f'Validation metric improved!! ({self.best_score:.6f} --> {score:.6f}).  Saving model ...')
            self.best_score = score
            self.save_checkpoint(score, model, save_path)
            self.counter = 0

    def save_checkpoint(self, score, model, save_path) -> None:
        '''Saves model when validation metric improves.'''
        self.best_metric = score

        model.save_pretrained(save_path)
        logger.info(f'Model saved at {save_path}')
        self.saved_models.append((save_path, score))

        if len(self.saved_models) > self.max_saves:
            self.saved_models.sort(key=lambda x: (x[1], x[0]), reverse=True) # Sort models by score, then by path
            lowest_f1_model = self.saved_models.pop()                 # Remove the model with the lowest score
            shutil.rmtree(lowest_f1_model[0])
            logger.info(f"Removed model with score at {lowest_f1_model[0]}")
        return

# train function
def train(model, optimizer, train_data, config, train_rel_types, eval_rel_types, eval_data=None, 
          num_steps=1000, eval_every=100, top_k=1, log_dir=None,
          wandb_log=False, wandb_sweep=False, warmup_ratio=0.1, train_batch_size=8, device='cuda', use_amp=True):

    # EarlyStopping
    max_saves = config.max_saves if hasattr(config, 'max_saves') else 3
    patience = config.early_stopping_patience if hasattr(config, 'early_stopping_patience') else None
    patience = patience if patience is not None else 100
    delta = config.early_stopping_delta if hasattr(config, 'early_stopping_delta') else 0.0
    delta = delta if delta is not None else 0.0
    early_stopping = EarlyStopping(patience=patience, delta=delta, max_saves=max_saves)


    if wandb_log:
        # Start a W&B Run with wandb.init
        wandb.login()
        run = wandb.init()
    else:
        run = None
    
    scaler = torch.cuda.amp.GradScaler(enabled=use_amp)

    model.train()

    # freeze params if requested
    if hasattr(config, 'num_layers_freeze') and config.num_layers_freeze is not None:
        model = freeze_n_layers(model, N=config.num_layers_freeze)

    # initialize data loaders
    train_loader = model.create_dataloader(train_data, batch_size=train_batch_size, shuffle=False, train_relation_types=train_rel_types)

    pbar = tqdm(range(num_steps))

    if warmup_ratio < 1:
        num_warmup_steps = int(num_steps * warmup_ratio)
    else:
        num_warmup_steps = int(warmup_ratio)

    if config.scheduler == "cosine_with_warmup":
        scheduler = get_cosine_schedule_with_warmup(
            optimizer,
            num_warmup_steps=num_warmup_steps,
            num_training_steps=num_steps
        )
    elif config.scheduler == "cosine_with_hard_restarts":
        scheduler = get_cosine_with_hard_restarts_schedule_with_warmup(
            optimizer,
            num_warmup_steps=num_warmup_steps,
            num_training_steps=num_steps,
            num_cycles=3
        )
    else:
        raise ValueError(f"Invalid scheduler: {config.scheduler}")

    iter_train_loader = iter(train_loader)

    prev_model_path = None

    accumulated_steps = 0 
    start = time.time()
    for step in pbar:
        try:
            x = next(iter_train_loader)
        except StopIteration:
            iter_train_loader = iter(train_loader)
            x = next(iter_train_loader)

        x = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in x.items()}


        with torch.autocast(device_type='cuda', dtype=torch.float16, enabled=use_amp):
            try:
                out = model(x)  # Forward pass
                loss, coref_loss, rel_loss = out['total_loss'], out.get('coref_loss', None), out.get('rel_loss', None)
            except Exception as e:
                logger.error(f"Error in step {step}: {e}")
                logger.error(f"Num tokens: {[len(x['tokens'][i]) for i in range(len(x['tokens']))]}")
                logger.error(f"Num relations: {[x['rel_label'][i].shape[0] for i in range(len(x['rel_label']))]}")
                logger.error(f"Num spans: {[x['span_idx'][i].shape[0] for i in range(len(x['span_idx']))]}")
                logger.error(f"Num candidate classes: {[len(x['classes_to_id'][i]) for i in range(len(x['classes_to_id']))]}")
                continue
        

        # check if loss is nan
        if torch.isnan(loss):
            logger.warning(f"Loss is NaN at step {step}")
            continue

        if config.gradient_accumulation is not None:
            loss = loss / config.gradient_accumulation  # Normalize the loss to account for the accumulation

        try:
            scaler.scale(loss).backward()  # Compute gradients
        except Exception as e:
            logger.error(f"Backprop Loss Error in step {step}: {e}")
            logger.error(f"Num tokens: {[len(x['tokens'][i]) for i in range(len(x['tokens']))]}")
            logger.error(f"Num relations: {[x['rel_label'][i].shape[0] for i in range(len(x['rel_label']))]}")
            logger.error(f"Num spans: {[x['span_idx'][i].shape[0] for i in range(len(x['span_idx']))]}")
            logger.error(f"Num candidate classes: {[len(x['classes_to_id'][i]) for i in range(len(x['classes_to_id']))]}")
            continue

        num_tokens = [len(x['tokens'][i]) for i in range(len(x['tokens']))]
        candidate_classes = [x['classes_to_id'][i] for i in range(len(x['classes_to_id']))]
        status = f"Step {step} | loss: {loss.item()}"
        if coref_loss is not None:
            status += f" | coref_loss: {coref_loss.item()} | rel_loss: {rel_loss.item()}"
        status += f" | x['rel_label']: {x['rel_label'].shape} | x['span_idx']: {x['span_idx'].shape} | x['tokens']: {num_tokens} | num candidate_classes: {[len(x['classes_to_id'][i]) for i in range(len(x['classes_to_id']))]}"
        logger.info(status)

        accumulated_steps += 1
        if config.gradient_accumulation is None or (accumulated_steps % config.gradient_accumulation == 0):
            # optimizer.step()        # Update parameters
            scaler.step(optimizer)
            scaler.update()
            scheduler.step()                        # Update learning rate schedule
            optimizer.zero_grad(set_to_none=True)   # Clear gradients after update (set_to_none=True here can modestly improve performance)
            accumulated_steps = 0                   # Reset accumulation counter


        description = f"step: {step} | epoch: {step // len(train_loader)} | loss: {loss.item():.2f}"


        if hasattr(config, 'save_at') and (step+1) in config.save_at:
            logger.info(f"Saving model at step {step+1}")
            current_path = os.path.join(log_dir, f'saved_at/model_{step + 1}')

            model.save_pretrained(current_path)

        if run is not None:
            run.log({
                "loss": loss.item(), 
                "num_relations": x['rel_label'].shape[1], 
                "num_tokens": max(num_tokens)
            })

        elif wandb_sweep:
            wandb.log(
                    {
                    "epoch": step // len(train_loader),
                    "train_loss": loss.item(),
                }
            )

        if (step + 1) % eval_every == 0:
            end = time.time()
            logger.info(f"Time taken for {eval_every} steps: {round(end - start)} seconds")
            start = time.time() # reset timer

            model.eval()

            current_path = os.path.join(log_dir, f'model_{step + 1}')

            # if there's no eval data, save the model and remove the previous one
            if eval_data is None:
                if prev_model_path:
                    shutil.rmtree(prev_model_path)

                model.save_pretrained(current_path)
                logger.info(f"Model saved at {current_path}")
                prev_model_path = current_path

            
            elif eval_data is not None:
                with torch.no_grad():

                    wandb_payload = {}

                    # (Re-)DocRED-specific testing
                    if config.dataset_name.lower() == 'redocred':
                        logger.info("Running testing...")
                        test_metrics = run_evaluation(
                            ckpt_dir=log_dir, use_gold_coref=True, 
                            use_auxiliary_coref=False, model=model)
                        test_log_string = "Step={step} | "
                        for k, v in test_metrics.items():
                            test_log_string += f"{k}: {v} | "
                        logger.info(test_log_string)
                        wandb_payload.update(test_metrics)
                    #######


                    logger.info('Evaluating...')
                    logger.info(f'Taking top k = {top_k} predictions for each relation...')

                    results, metric_dict = model.evaluate(
                        eval_data, 
                        flat_ner=True, 
                        threshold=config.eval_threshold, 
                        batch_size=config.eval_batch_size,
                        relation_types=eval_rel_types if config.fixed_relation_types else [],
                        top_k=top_k,
                        dataset_name=config.dataset_name
                    )
                    micro_f1, micro_precision, micro_recall = metric_dict['micro_f1'], metric_dict['micro_precision'], metric_dict['micro_recall']
                    macro_f1, macro_precision, macro_recall = metric_dict['macro_f1'], metric_dict['macro_precision'], metric_dict['macro_recall']
                    logger.info(f"Best threshold for eval: {metric_dict['best_threshold']}")

                    wandb_payload.update({
                                "epoch": step // len(train_loader),
                                "eval_f1_micro": micro_f1,

*Content truncated for brevity.*

```

## File: eval.py

<a name='file-eval.py'></a>
*Description*: This is a Python script.

```python
import argparse
import os

import torch
from tqdm import tqdm
from transformers import get_cosine_schedule_with_warmup, get_cosine_with_hard_restarts_schedule_with_warmup

# from model_nested import NerFilteredSemiCRF
from glirel import GLiREL
from glirel.modules.run_evaluation import sample_train_data
from glirel.model import load_config_as_namespace
from datetime import datetime
import json
import logging
import random
import shutil
import wandb
from functools import partial
from sklearn.model_selection import train_test_split
import time
import gc


logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])

'''

python eval.py --ckpt-dir logs/docred/docred-2024-09-16__13-06-14/model_19500 \
    --eval-data data/redocred_test.jsonl

'''

def create_parser():
    parser = argparse.ArgumentParser(description="Zero-shot Relation Extraction")
    parser.add_argument("--ckpt-dir", type=str, help="Path to model checkpoint directory")
    parser.add_argument("--eval-data", type=str, help="Path to evaluation data")
    return parser


def get_unique_relations(data):
    unique_rel_types = []
    for item in data:
        for r in item['relations']:
            unique_rel_types.append(r["relation_text"])
    unique_rel_types = list(set(unique_rel_types))
    return unique_rel_types



def split_data_by_relation_type(data, num_unseen_rel_types):
    """
    Attempts to split a dataset into training and testing sets based on relation types,
    aiming to have a specified number of unique relation types exclusively in the test set
    to simulate a zero-shot learning scenario. The function shuffles and splits the relation
    types, allocating the first chunk as unseen relation types for testing and the rest for training.
    
    It iteratively adjusts the number of unseen relation types if the initial split does not achieve
    the desired number of unique test relation types, retrying with an incremented number until it succeeds
    or the number reaches twice the original request, resetting as needed.

    Notes:
        - This function relies heavily on the assumption that sufficient relation diversity exists
          to meet the zero-shot criteria. If not, the test set may not end up with the intended
          number of unique unseen relation types.
        - The function can potentially skip a significant number of items that contain both train and
          test relation types, leading to data wastage.
        - The iterative process to adjust unseen relation types may lead to computational inefficiency,
          especially for large datasets with diverse relations.
    """

    unique_relations = get_unique_relations(data)
    correct_num_unseen_relations_achieved = False
    original_num_unseen_rel_types = num_unseen_rel_types

    logger.info(f"Running dataset splitting...")
    start = time.time()
    count = 0
    while not correct_num_unseen_relations_achieved:
        seed = random.randint(0, 1000)
        random.seed(seed)
        random.shuffle(unique_relations)
        test_relation_types = set(unique_relations[ : num_unseen_rel_types ])
        train_relation_types = set(unique_relations[ num_unseen_rel_types : ])
        
        train_data = []
        test_data = []
        skipped_items = []
        
        # Splitting data based on relation types
        for item in data:
            relation_types = {r["relation_text"] for r in item['relations']}
            if relation_types.issubset(test_relation_types):
                test_data.append(item)
            elif relation_types.issubset(train_relation_types):
                train_data.append(item)
            else:
                # Entries that contain both train and test relation types are currently skipped
                skipped_items.append(item)
        
        # if we have the right number of eval relations, break
        if len(get_unique_relations(test_data)) == original_num_unseen_rel_types: 
            correct_num_unseen_relations_achieved = True
        else:
            # bump the number of unseen relations by 1 to cast a wider net
            # if the bump gets too big, reset it
            num_unseen_rel_types = num_unseen_rel_types + 1 if (num_unseen_rel_types <  original_num_unseen_rel_types*2) else num_unseen_rel_types
        # logger.info('Incorrect number of unseen relation types. Retrying...')

        count += 1
        if count % 50 == 0:
            logger.info(f"Attempt {count} | Seed {seed}")

    if len(skipped_items) > 0:
        logger.info(f"Skipped items: {len(skipped_items)} because they have __BOTH__ train and test relation types")
    
    logger.info(f"Split on seed {seed}")
    logger.info(f"Splitting took {time.time() - start} seconds")
    return train_data, test_data

    
def dirty_split_data_by_relation_type(data, num_unseen_rel_types, max_test_size):
    '''
    This function does not care if the interesection of train and test relation types is empty.
    Used for custom datasets to avoid having a large number of eval classes (causes OOM), 
    and I do not mind if the eval set has some train classes.
    '''
    logger.info("Dirty splitting data...")

    unique_relations = get_unique_relations(data)
    correct_num_unseen_relations_achieved = False
    original_num_unseen_rel_types = num_unseen_rel_types


    while not correct_num_unseen_relations_achieved:
        seed = random.randint(0, 1000)
        random.seed(seed)
        random.shuffle(unique_relations)
        test_relation_types = set(unique_relations[ : num_unseen_rel_types ])
        
        train_data = []
        test_data = []

        # Splitting data based on relation types
        for item in data:
            relation_types = {r["relation_text"] for r in item['relations']}
            if len(test_data) < max_test_size and any([rel in test_relation_types for rel in relation_types]):
                test_data.append(item)
            else:
                train_data.append(item)

        # if we have the right number of eval relations, break
        if len(get_unique_relations(test_data)) == original_num_unseen_rel_types or len(test_data) >= max_test_size: 
            correct_num_unseen_relations_achieved = True
        else:
            # bump the number of unseen relations by 1 to cast a wider net
            # if the bump gets too big, reset it
            num_unseen_rel_types = num_unseen_rel_types + 1 if (num_unseen_rel_types <  original_num_unseen_rel_types*2) else num_unseen_rel_types


    return train_data, test_data


# train function
def eval(model, config, eval_rel_types, eval_data, 
         top_k=1,
         device='cuda', use_amp=True):

        model.eval()
    
        with torch.no_grad():

            logger.info('Evaluating...')
            logger.info(f'Taking top k = {top_k} predictions for each relation...')

            results, metric_dict = model.evaluate(
                eval_data, 
                flat_ner=True, 
                threshold=config.eval_threshold, 
                batch_size=config.eval_batch_size,
                relation_types=eval_rel_types if config.fixed_relation_types else [],
                top_k=top_k
            )
            micro_f1, micro_precision, micro_recall = metric_dict['micro_f1'], metric_dict['micro_precision'], metric_dict['micro_recall']
            macro_f1, macro_precision, macro_recall = metric_dict['macro_f1'], metric_dict['macro_precision'], metric_dict['macro_recall']


            logger.info(f"Results = {results}")


        torch.cuda.empty_cache()  # Clear cache after evaluation to prepare for training
        gc.collect()


def main(args):

    # load config
    config_path = args.ckpt_dir + '/glirel_config.json'
    with open(config_path, 'r') as f:
        config_dict = json.load(f)
        config = argparse.Namespace(**config_dict)

    if args.eval_data is not None:
        config.eval_data = args.eval_data

    # set up logging
    current_time = datetime.now().strftime("%Y-%m-%d__%H-%M-%S")
    config.log_dir = f'logs/{config.dataset_name}/{config.dataset_name}-{current_time}'
    if not os.path.exists(config.log_dir):
        os.makedirs(config.log_dir)

    log_file = "eval.log"
    log_file_path = os.path.join(config.log_dir, log_file)
    if os.path.exists(log_file_path):
        os.remove(log_file_path)
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info("🚀 Relation extraction evlauation started")
    logger.info(f"Evaluating on file {config.eval_data}")



    # Prep data

    if isinstance(config.train_data, str):
        config.train_data = [config.train_data]

    train_data = []
    for train_subset in config.train_data:
        if train_subset.endswith('.jsonl'):
            with open(train_subset, 'r') as f:
                train_subset = [json.loads(line) for line in f]
                # train_subset = []
                # for i in range(1_000):
                #     train_subset.append(json.loads(next(f)))
        elif train_subset.endswith('.json'):
            with open(train_subset, 'r') as f:
                train_subset = json.load(f)
        else:
            raise ValueError(f"Invalid data format: {config.train_data}")
        train_data.extend(train_subset)
    data = train_data



    if hasattr(config, 'eval_data'):

        if isinstance(config.eval_data, str):
            config.eval_data = [config.eval_data]

        eval_data = []
        for eval_subset in config.eval_data:
            if eval_subset.endswith('.jsonl'):
                with open(eval_subset, 'r') as f:
                    eval_subset = [json.loads(line) for line in f]
            elif eval_subset.endswith('.json'):
                with open(eval_subset, 'r') as f:
                    eval_subset = json.load(f)
            else:
                raise ValueError(f"Invalid data format: {config.eval_data}. Must be .jsonl or .json")
            eval_data.extend(eval_subset)

    else:
        eval_data = None


    # train / eval split

    if eval_data is None:
        if args.skip_splitting:
            print("Skipping dataset splitting. Randomly splitting data into train and eval sets.")
            data = sorted(data, key=lambda x: len(x['relations']))
            
        elif config.num_unseen_rel_types is not None:

            if 'zero_rel' in config.dataset_name:
                file_name = 'data/wiki_zsl_all.jsonl'
                config.eval_data = file_name
                with open(file_name, 'r') as f:
                    logger.info(f"Generating eval split from {file_name}...")
                    eval_data = [json.loads(line) for line in f]
                _, eval_data = split_data_by_relation_type(eval_data, config.num_unseen_rel_types)
                data = sorted(data, key=lambda x: len(x['relations']))
                train_data = data
            else:
                train_data, eval_data = split_data_by_relation_type(data, config.num_unseen_rel_types)
        else:
            raise ValueError("No eval data provided and config.num_unseen_rel_types is None")
    else:
        eval_data = eval_data
        train_data = data

    train_rel_types = get_unique_relations(train_data)
    eval_rel_types = get_unique_relations(eval_data) if eval_data is not None else None
    logger.info(f"Num Train relation types: {len(train_rel_types)}")
    logger.info(f"Number of train samples: {len(train_data)}")
    if eval_data is not None:
        logger.info(f"Intersection: {set(train_rel_types) & set(eval_rel_types)}")
        logger.info(f"Num Eval relation types: {len(eval_rel_types)}")
        logger.info(f"Number of eval samples: {len(eval_data)}")


    # Load model
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = GLiREL.from_pretrained(args.ckpt_dir, map_location=device)
    model.config = config

    # Get number of parameters (trainable and total)
    num_params = sum(p.numel() for p in model.parameters())
    num_trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    logger.info(f"Number of trainable parameters: {num_trainable_params} / {num_params}")

    use_amp = device != 'cpu' 
    model = model.to(device)

    logger.info(f"Using config: \n{json.dumps(config.__dict__, indent=2)}\n\n")


    eval(model, config, eval_rel_types=eval_rel_types, eval_data=eval_data,
          top_k=config.top_k,
          device=device)


if __name__ == "__main__":
    # parse args
    parser = create_parser()
    args = parser.parse_args()

    main(args)

```

## File: RELEASE.md

<a name='file-RELEASE.md'></a>
*Description*: No specific description available.

```plaintext
# A guide to making a release

This guide collects the steps we do in GLiREL to make a release on PyPI. They result from (variations of) hard-learned lessons and while following this guide is completely optional, it’s strongly recommended to do so. 🙂 This is a truncated version of the [SetFit](https://github.com/huggingface/setfit/blob/main/RELEASE.md) release guide, which is more exhaustive and does some additional steps.

### Preparation

```bash
pip install build twine
```

To be able to make a release for a given project, you’ll need an account on [PyPI](https://pypi.org/) and on [Test PyPI](https://test.pypi.org/). If you are making a release for an existing project, your username will need to be added to that project by one of the current maintainers on PyPI. Note that we strongly recommend enabling two-factor authentication on PyPI.

Additionally, it can be nice to familiarize yourself with [Semantic Versioning](https://semver.org/). This is a fairly strict document, but it provides a useful summary that library maintainers should follow:

> Given a version number MAJOR.MINOR.PATCH, increment the:
> 
> 1. MAJOR version when you make incompatible API changes
> 2. MINOR version when you add functionality in a backward compatible manner
> 3. PATCH version when you make backward compatible bug fixes
> 
> Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

The very first release should be "0.1.0".

## Releases

### Step 1: Adjust the version of your package

You should have the current version specified in [`glirel/__init__.py`](glirel/__init__.py). This version should be a dev version (e.g. `0.1.0.dev`) before you release, change it to the name of the version you are releasing:

```diff
- __version__ = "0.4.0.dev"
+ __version__ = "0.4.0"
```

Commit the changes on your release branch and push them:

```bash
git add glirel
git commit -m "Release: v{VERSION}"
git push -u origin main
```

### Step 2: (Optional) Make sure all tests pass

If you add tests, then you should also add CI, e.g. like this [`tests.yaml`](https://github.com/tomaarsen/SpanMarkerNER/blob/main/.github/workflows/tests.yaml) file. This will automatically run tests whenever you make changes, it can be very useful. Make sure all tests that you may have pass before proceeding to the next step.

### Step 3: Add a tag for your release

A tag will flag the exact commit associated to your release (and be easier to remember than the commit hash!). The tag should be `v<VERSION>` so for instance `v4.12.0`. 

Here is how you can create and push your tag:

```bash
git tag v<VERSION>
git push --tags origin main
```

### Step 4: (Optional) Prepare the release notes

You can then put your release notes in a Draft Release on GitHub, in [https://github.com/jackboyla/GLiREL/releases](https://github.com/jackboyla/GLiREL/releases) and write a small paragraph highlighting each of the new features this release is adding.

You can use the previously created tag to let GitHub auto-generate some release notes based on recent pull requests.

### Step 5: Create the wheels for your release

This is what you'll upload on PyPI and what everyone will download each time they `pip install` your package.

Clean previous builds by deleting the `build` and `dist` directories or by running:

```
rm -rf build && rm -rf dist
```

Then run:

```bash
python -m build
```

This will create two folders, `build` and a `dist` with the new versions of your package. These contain a 1) source distribution and a 2) wheel.

### Step 6: Upload your package on PyPI test

**DO NOT SKIP THIS STEP!**

This is the most important check before actually releasing your package in the wild. Upload the package on PyPI test and check you can properly install it.

To upload it:

```bash
twine upload dist/* -r pypitest --repository-url=https://test.pypi.org/legacy/
```

You will be prompted for your username and password. 

If that doesn't work, you can create an API Token for your Test PyPI account and create a `~/.pypirc` account if it doesn't already exist, with:

```
[distutils]
  index-servers =
    glirel_test

[glirel_test]
  repository = https://test.pypi.org/legacy/
  username = __token__
  password = pypi-...
```
(some more details on this [here](https://pypi.org/help/#apitoken))

And then run:
```bash
twine upload dist/* -r glirel_test
```

Once that has uploaded the package, in a fresh environment containing all dependencies you need (tip: you can use Google Colab for this!), try to install your new package from the PyPI test server. First install all dependencies, and then your package.

```bash
python -m pip install torch transformers huggingface_hub flair seqeval tqdm
python -m pip install -i https://test.pypi.org/simple/ glirel
```

If everything works, you should be able to run this code:

```python
from glirel import GLiREL
import spacy

model = GLiREL.from_pretrained("jackboyla/glirel_base")

text = "Jack Dorsey's father, Tim Dorsey, is a licensed pilot. Jack met his wife Sarah Paulson in New York in 2003. They have one son, Edward."

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)

labels = ['country of origin', 'licensed to broadcast to', 'parent', 'followed by', 'located in or next to body of water', 'spouse', 'child']

tokens = [token.text for token in doc]

ner = [[ent.start, ent.end, ent.label_, ent.text] for ent in doc.ents]
print(f"Entities detected: {ner}")

relations = model.predict_relations(tokens, labels, threshold=0.01, ner=ner)

print('Number of relations:', len(relations))

sorted_data_desc = sorted(relations, key=lambda x: x['score'], reverse=True)
print("\nDescending Order by Score:")
for item in sorted_data_desc:
    print(f"{item['head_text']} --> {item['label']} --> {item['tail_text']} | socre: {item['score']}")

```

### Step 7: Publish on PyPI

This cannot be undone if you messed up, so make sure you have run Step 6!

Once you’re fully ready, upload your package on PyPI:

```bash
twine upload dist/* -r pypi
```

You will be prompted for your username and password, unless you're using the recommended [PyPI API token](https://pypi.org/help/#apitoken). 

### Step 8: (Optional) Publish your release notes

Go back to the draft you did at step 4 ([https://github.com/jackboyla/GLiREL/releases](https://github.com/jackboyla/GLiREL/releases)) and publish them.

### Step 9: Bump the dev version on the main branch

You’re almost done! Just go back to the `main` branch and change the dev version in [`glirel/__init__.py`](glirel/__init__.py) to the new version you’re developing, for instance `4.13.0.dev` if just released `4.12.0`.

```

## File: visualise.py

<a name='file-visualise.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding: utf-8

# ## WikiZSL

# In[52]:


import matplotlib.pyplot as plt

# Data
categories = ['Refine prompt + relation', 'Refine prompt only', 'Refine relation only', 'No refinement']
f1_scores = [54.16, 65.67, 67.37, 73.91]
colors = ['#ff9999', '#99cc66', '#66cccc', '#cc99ff']
hatches = ['/', 'x', '-', '|']

# Increase figure size to accommodate long category names
fig, ax = plt.subplots(figsize=(10, 4))  

# Plot
bars = ax.barh(categories, f1_scores, color=colors)

# Add hatches
for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)
    bar.set_rasterized(True) 

# Add text annotations at the end of each bar
for bar in bars:
    ax.text(bar.get_width() + 0.3,  # Adding 0.3 to move text outside the bar
            bar.get_y() + bar.get_height() / 2,
            f'{bar.get_width():.2f}', va='center', ha='left', color='black', fontsize=17)

# Label and styling
plt.xlabel('Mean Macro F1', fontweight='light', fontsize=18)
plt.xlim(50, 77)

# Adjust y-tick labels font size
# ax.set_yticklabels(categories, fontsize=15)  # You can adjust the size

# Adjust ticks font size
ax.tick_params(axis='both', which='major', labelsize=15)


# Adjust layout
plt.tight_layout()  # Ensures everything fits into the figure neatly

plt.savefig('figs/refine-ablation-wiki-zsl.pdf', format='pdf', bbox_inches='tight', dpi=300)

# Show plot
plt.show()


# ## FewREL

# In[51]:


import matplotlib.pyplot as plt

# Data
categories = ['Refine prompt + relation', 'Refine prompt only', 'Refine relation only', 'No refinement']
f1_scores = [84.48, 80.98, 77.43, 81.29]
colors = ['#1abc9c', '#e91e63', '#f1c40f', '#2980b9'] 
hatches = ['/', 'x', '-', '|']

# Increase figure size to accommodate long category names
fig, ax = plt.subplots(figsize=(10, 4))  

# Plot
bars = ax.barh(categories, f1_scores, color=colors)

# Add hatches
for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)
    bar.set_rasterized(True) 

# Add text annotations at the end of each bar
for bar in bars:
    ax.text(bar.get_width() + 0.3,  # Adding 0.3 to move text outside the bar
            bar.get_y() + bar.get_height() / 2,
            f'{bar.get_width():.2f}', va='center', ha='left', color='black', fontsize=17)

# Label and styling
plt.xlabel('Mean Macro F1', fontweight='light', fontsize=18)
plt.xlim(70, 87)

# Adjust y-tick labels font size
# ax.set_yticklabels(categories, fontsize=15)  # You can adjust the size

# Adjust ticks font size
ax.tick_params(axis='both', which='major', labelsize=15)


# Adjust layout
plt.tight_layout()  # Ensures everything fits into the figure neatly

plt.savefig('figs/refine-ablation-few-rel.pdf', format='pdf', bbox_inches='tight', dpi=300)

# Show plot
plt.show()


# ## Random drop

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# Data: Scores for two datasets under two conditions (with drop, without drop)
datasets = ['FewRel', 'WikiZSL']
with_drop = [81.29, 73.91]  # Scores for "with random drop"
without_drop = [84.48, 71.31]  # Scores for "without random drop"

# Bar width and position
bar_width = 0.35
index = np.arange(len(datasets))

# Create the plot
fig, ax = plt.subplots(figsize=(10, 4))

# Plot bars for "with drop" and "without drop" conditions
bars1 = ax.bar(index, with_drop, bar_width, label='With Drop', color='#f39c12', hatch='/')
bars2 = ax.bar(index + bar_width, without_drop, bar_width, label='Without Drop', color='#3498db', hatch='x')

# Add text annotations
for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
            f'{bar.get_height():.2f}', ha='center', va='bottom', fontsize=10)
    bar.set_rasterized(True) 
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
            f'{bar.get_height():.2f}', ha='center', va='bottom', fontsize=10)
    bar.set_rasterized(True) 

# Add labels, title, and legend
# ax.set_xlabel('Datasets', fontweight='bold', fontsize=12)
ax.set_ylabel('Mean Macro F1', fontweight='bold', fontsize=15)
# ax.set_title('Effect of Random Dropping on Two Datasets', fontweight='bold', fontsize=14)
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(datasets)
ax.legend()

ax.tick_params(axis='both', which='major', labelsize=15)

# Tight layout and save
plt.ylim(60, 88)
plt.tight_layout()
plt.savefig('figs/random-drop-ablation.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.show()


# In[ ]:





# In[ ]:


import spacy
from spacy.tokens import Span
from spacy import displacy

def visualize_relation(text, relations):
    nlp = spacy.blank("en")
    doc = nlp(text)

    # Manually set dependency relations to visualize relations
    for token in doc:
        token.dep_ = "dep"  # default to 'dep'

    spans = []
    # Calculate character offsets for each entity
    for rel in relations:
        head = Span(doc, rel['head_pos'][0], rel['head_pos'][1], label=rel['head_text'])
        tail = Span(doc, rel['tail_pos'][0], rel['tail_pos'][1], label=rel['tail_text'])

        doc.ents += (head, tail)

        # Mock dependencies
        head_root = head.root
        tail_root = tail.root

        head_root.dep_ = "rel"  # Relation type can be customized
        head_root.head = tail_root  # Point head to tail

    options = {"fine_grained": True}
    displacy.render(doc, style="dep", options=options, jupyter=True)

# Example data
text = "Binsey located in or next to body of water River Thames"
relations = [
    {'head_pos': [0, 1], 'tail_pos': [9, 11], 'head_text': 'Binsey', 'tail_text': 'River Thames', 'label': 'located in or next to body of water', 'score': 0.9235768914222717},
    # {'head_pos': [9, 11], 'tail_pos': [0, 1], 'head_text': 'River Thames', 'tail_text': 'Binsey', 'label': 'located in or next to body of water', 'score': 0.12615662813186646}
]

visualize_relation(text, relations)


# In[ ]:





```

## File: glirel/__init__.py

<a name='file-glirel-__init__.py'></a>
*Description*: This is a Python script.

```python
__version__ = "1.0.1"

from .model import GLiREL
from typing import Optional, Union, List
import torch

__all__ = ["GLiREL"]


# https://github.com/tomaarsen/SpanMarkerNER/blob/main/span_marker/__init__.py
# Set up for spaCy
try:
    from spacy.language import Language
except ImportError:
    pass
else:

    DEFAULT_SPACY_CONFIG = {
        "model": "jackboyla/glirel-large-v0",
        "batch_size": 1,
        "device": None,
        "threshold": 0.3,
    }

    @Language.factory(
        "glirel",
        assigns=["doc._.relations"],
        default_config=DEFAULT_SPACY_CONFIG,
    )
    def _spacy_glirel_factory(
        nlp: Language,
        name: str, 
        model: str,
        batch_size: int,
        device: Optional[Union[str, torch.device]],
        threshold: float,
    ) -> "SpacyGLiRELWrapper":
        from glirel.spacy_integration import SpacyGLiRELWrapper
        return SpacyGLiRELWrapper(model, batch_size=batch_size, device=device)
```

## File: glirel/model.py

<a name='file-glirel-model.py'></a>
*Description*: This is a Python script.

```python
import argparse
import json
from pathlib import Path
import re
import os
from typing import Dict, Optional, Union
import numpy as np
import torch
import torch.nn.functional as F
import yaml
import time
from tqdm import tqdm
import glirel
from glirel.modules.layers import LstmSeq2SeqEncoder, ScorerLayer, FilteringLayer, RefineLayer
from glirel.modules.base import InstructBase
from glirel.modules.evaluator import greedy_search, RelEvaluator
from glirel.modules.span_rep import SpanRepLayer
from glirel.modules.rel_rep import RelRepLayer
from glirel.modules.token_rep import TokenRepLayer
from glirel.modules import loss_functions
from torch import nn
from torch.nn.utils.rnn import pad_sequence
from huggingface_hub import PyTorchModelHubMixin, hf_hub_download
from huggingface_hub.utils import HfHubHTTPError
from typing import List, Dict, Union
from loguru import logger


class GLiREL(InstructBase, PyTorchModelHubMixin):
    def __init__(self, config):
        super().__init__(config)

        self.config = config

        # [REL] token
        self.rel_token = "[REL]"
        self.sep_token = "[SEP]"

        label_embed_strategies = ['ent_token', 'label', 'both']
        assert self.config.label_embed_strategy in label_embed_strategies, f"Invalid label_embed_strategy: {self.config.label_embed_strategy}. Must be one of {label_embed_strategies}"

        self.positive_weight = getattr(self.config, 'positive_weight', 2.0)  # weight for positive labels (Default: 2.0)
        self.negative_weight = getattr(self.config, 'negative_weight', 1.0)  # weight for negative labels (Default: 1.0)

        self.threshold_search_metric = getattr(self.config, 'threshold_search_metric', 'micro_f1')  # metric to use for threshold search (Default: 'micro_f1')

        # usually a pretrained bidirectional transformer, returns first subtoken representation
        # add_tokens = [self.rel_token, self.sep_token]
        add_tokens = [self.rel_token, self.sep_token, self.base_config.entity_start_token, self.base_config.entity_end_token]
        if hasattr(self.base_config, "entity_start_token"):
            add_tokens += self.base_config.entity_start_token, self.base_config.entity_end_token
        self.token_rep_layer = TokenRepLayer(model_name=config.model_name, fine_tune=config.fine_tune,
                                             subtoken_pooling=config.subtoken_pooling, hidden_size=config.hidden_size,
                                             add_tokens=add_tokens)

        # hierarchical representation of tokens (zaratiana et al, 2022)
        # https://arxiv.org/pdf/2203.14710.pdf
        self.rnn = LstmSeq2SeqEncoder(
            input_size=config.hidden_size,
            hidden_size=config.hidden_size // 2,
            num_layers=1,
            bidirectional=True,
        )


        self.span_rep_layer = RelRepLayer(
            rel_mode=config.rel_mode,
            span_mode=config.span_marker_mode,
            hidden_size=config.hidden_size,
            max_width=config.max_width,
            dropout=config.dropout,
        )

        # prompt representation (FFN)
        self.prompt_rep_layer = nn.Sequential(
            nn.Linear(config.hidden_size, config.hidden_size * 4),
            nn.Dropout(config.dropout),
            nn.ReLU(),
            nn.Linear(config.hidden_size * 4, config.hidden_size)
        )

        # refine relation representation
        if hasattr(config, "refine_relation") and config.refine_relation:
            self.refine_relation = RefineLayer(
                config.hidden_size, config.hidden_size // 64, num_layers=1, ffn_mul=config.ffn_mul,
                dropout=config.dropout,
                read_only=True
            )

        # refine prompt representation
        if hasattr(config, "refine_prompt") and config.refine_prompt:
            self.refine_prompt = RefineLayer(
                config.hidden_size, config.hidden_size // 64, num_layers=2, ffn_mul=config.ffn_mul,
                dropout=config.dropout,
                read_only=True
            )


        # coreference resolution
        if getattr(config, "coref_classifier", False):
            self.coref_classifier = nn.Sequential(
                nn.Linear(config.hidden_size, config.hidden_size),
                nn.Dropout(config.dropout),
                nn.ReLU(),
                nn.Linear(config.hidden_size, 1)
            )


        # scoring layer
        self.scorer = ScorerLayer(config.scorer, hidden_size=config.hidden_size, dropout=config.dropout)


    def get_optimizer(self, lr_encoder, lr_others, freeze_token_rep=False):
        """
        Parameters:
        - lr_encoder: Learning rate for the encoder layer.
        - lr_others: Learning rate for all other layers.
        - freeze_token_rep: whether the token representation layer should be frozen.
        """
        param_groups = [
            # encoder
            {'params': self.rnn.parameters(), 'lr': lr_others},
            {'params': self.span_rep_layer.parameters(), 'lr': lr_others},
            {'params': self.prompt_rep_layer.parameters(), 'lr': lr_others},
            {"params": self._rel_filtering.parameters(), "lr": lr_others},
            {'params': self.scorer.parameters(), 'lr': lr_others}
        ]

        if not freeze_token_rep:
            # If token_rep_layer should not be frozen, add it to the optimizer with its learning rate
            param_groups.append({'params': self.token_rep_layer.parameters(), 'lr': lr_encoder})
        else:
            # If token_rep_layer should be frozen, explicitly set requires_grad to False for its parameters
            for param in self.token_rep_layer.parameters():
                param.requires_grad = False

        optimizer = torch.optim.AdamW(param_groups)

        return optimizer

    def compute_score(self, x):

        span_idx = x['span_idx'] * x['span_mask'].unsqueeze(-1).to(self.device)  # ([B, num_possible_spans, 2])  *  ([B, num_possible_spans, 1])

        new_length = x['seq_length'].clone()
        new_tokens = []
        all_len_prompt = []
        num_classes_all = []

        # add prompt to the tokens
        for i in range(len(x['tokens'])):
            all_types_i = list(x['classes_to_id'][i].keys())
            # multiple entity types in all_types. Prompt is appended at the start of tokens
            entity_prompt = []
            num_classes_all.append(len(all_types_i))
            # add enity types to prompt
            for relation_type in all_types_i:
                entity_prompt.append(self.rel_token)     # [REL] token
                entity_prompt.append(relation_type)        # relation type
            entity_prompt.append(self.sep_token)         # [SEP] token

            # prompt format:
            # [REL] relation_type [REL] relation_type ... [REL] relation_type [SEP]

            # add prompt to the tokens
            tokens_p = entity_prompt + x['tokens'][i]

            # input format:
            # [REL] relation_type_1 [REL] relation_type_2 ... [REL] relation_type_m [SEP] token_1 token_2 ... token_n

            # update length of the sequence (add prompt length to the original length)
            new_length[i] = new_length[i] + len(entity_prompt)
            # update tokens
            new_tokens.append(tokens_p)
            # store prompt length
            all_len_prompt.append(len(entity_prompt))

        # create a mask using num_classes_all (False, if it exceeds the number of classes, True otherwise)
        max_num_classes = max(num_classes_all)
        rel_type_mask = torch.arange(max_num_classes).unsqueeze(0).expand(len(num_classes_all), -1).to(
            x['span_mask'].device)
        rel_type_mask = rel_type_mask < torch.tensor(num_classes_all).unsqueeze(-1).to(
            x['span_mask'].device)  # [batch_size, max_num_classes]

        # compute all token representations
        bert_output = self.token_rep_layer(new_tokens, new_length)
        word_rep_w_prompt = bert_output["embeddings"]  # embeddings for all tokens (with prompt)
        mask_w_prompt = bert_output["mask"]  # mask for all tokens (with prompt)

        # get word representation (after [SEP]), mask (after [SEP]) and relation type representation (before [SEP])
        word_rep = []      # word representation (after [SEP])
        mask = []          # mask (after [SEP])
        rel_type_rep = []  # relation type representation (before [SEP])
        for i in range(len(x['tokens'])):
            prompt_entity_length = all_len_prompt[i]  # length of prompt for this example
            # get word representation (after [SEP])
            word_rep.append(word_rep_w_prompt[i, prompt_entity_length:prompt_entity_length + x['seq_length'][i]])
            # get mask (after [SEP])
            mask.append(mask_w_prompt[i, prompt_entity_length:prompt_entity_length + x['seq_length'][i]])

            # get entity type representation (before [SEP])
            relation_rep = word_rep_w_prompt[i, :prompt_entity_length - 1]  # remove [SEP]
            if self.config.label_embed_strategy == 'ent_token':
                # Only use class token ([REL]) embeddings (every second element starting from 0)
                relation_rep = relation_rep[0::2]
            elif self.config.label_embed_strategy == 'label':
                # Only use label embeddings (every second element starting from 1)
                relation_rep = relation_rep[1::2]
            elif self.config.label_embed_strategy == 'both':
                # Interleave [REL] tokens and label embeddings
                relation_rep = relation_rep.reshape(-1, 2, relation_rep.shape[-1]).mean(dim=1)  # Take the mean of each [REL] and label embedding pair
            rel_type_rep.append(relation_rep)

        # padding for word_rep, mask and rel_type_rep
        word_rep = pad_sequence(word_rep, batch_first=True)          # [B, seq_len, D]
        mask = pad_sequence(mask, batch_first=True)                  # [B, seq_len]
        rel_type_rep = pad_sequence(rel_type_rep, batch_first=True)  # [B, len_types, D]

        # compute span representation
        word_rep = self.rnn(word_rep, mask)                  # ([B, seq_length, D])
        rel_rep = self.span_rep_layer(word_rep, span_idx=span_idx, relations_idx=x['relations_idx'])    # ([B, num_pairs, D])

        # compute final entity type representation (FFN)
        rel_type_rep = self.prompt_rep_layer(rel_type_rep)   # (B, len_types, D)
        num_classes = rel_type_rep.shape[1]                  # number of relation types


        # refine relation representation ##############################################
        relation_classes = x['rel_label']  # [B, num_entity_pairs]
        rel_rep_mask = relation_classes > 0
        ################################################################################

        if hasattr(self, "refine_relation"):
            # refine relation representation
            rel_rep = self.refine_relation(
                rel_rep, word_rep, rel_rep_mask, mask
            )

        if hasattr(self, "refine_prompt"):
            # refine relation representation with relation type representation ############
            rel_type_rep = self.refine_prompt(
                rel_type_rep, rel_rep, rel_type_mask, rel_rep_mask
            )
        ################################################################################


        # Coreference Resolution ##############################
        if hasattr(self, "coref_classifier"):
            coref_scores = self.coref_classifier(rel_rep)  # (B, num_pairs, 1)
        else:
            coref_scores = None
        #######################################################
        
        # similarity score
        scores = self.scorer(rel_rep, rel_type_rep) # ([B, num_pairs, num_classes])

        return scores, num_classes, rel_type_mask, coref_scores  # ([B, num_pairs, num_classes]), num_classes, ([B, num_classes]), ([B, num_pairs, 1])


    def compute_coref_loss(self, coref_scores, coref_ground_truth):

        coref_loss = F.binary_cross_entropy_with_logits(coref_scores, coref_ground_truth)

        return coref_loss

    def compute_relation_loss(self, logits_label, labels_one_hot):

        if self.config.loss_func == "binary_cross_entropy_loss":
            # compute loss (without reduction)
            all_losses = F.binary_cross_entropy_with_logits(
                logits_label, 
                labels_one_hot,
                reduction='none'
            )
        elif self.config.loss_func == "focal_loss":
            # might make it better at long-tail, but overall metrics may become worse
            all_losses = loss_functions.focal_loss_with_logits(
                logits_label, 
                labels_one_hot,
                alpha=self.config.alpha,
                gamma=self.config.gamma,
                reduction='none'
            )
        else:
            raise ValueError(f"Invalid loss function: {self.config.loss_func}")
        
        return all_losses


    def forward(self, x):
        # compute span representation
        scores, num_classes, rel_type_mask, coref_scores = self.compute_score(x)
        batch_size = scores.size(0)


        # loss for filtering classifier
        logits_label = scores.view(-1, num_classes)

        labels = x['rel_label'].view(-1)     # [B * num_entity_pairs]

        # mask for coreference and relation labels
        coref_mask = (labels <= -50) 
        labels[coref_mask] = (labels[coref_mask] // -50).long()                
        rel_mask = (labels != -1)   # Exclude padding (and coreference) labels

        # separate labels for relation classification
        rel_labels = labels.masked_fill(~rel_mask, 0)  # Set non-relation labels to 0

        # one-hot encoding
        labels_one_hot = torch.zeros(labels.size(0), num_classes + 1, dtype=torch.float32).to(scores.device) # ([batch_size * num_spans, num_classes + 1])
        labels_one_hot.scatter_(1, rel_labels.unsqueeze(1), 1) # Set the corresponding index to 1
        labels_one_hot = labels_one_hot[:, 1:]                 # Remove the first column
        # Shape of labels_one_hot: (batch_size * num_spans, num_classes)

        all_losses = self.compute_relation_loss(logits_label, labels_one_hot)
        
        # Mask and weight relation classification loss
        # mask loss using rel_type_mask (B, C)
        masked_loss = all_losses.view(batch_size, -1, num_classes) * rel_type_mask.unsqueeze(1)   #  ([B, L*K, num_classes])  *  ([B, 1, num_classes])
        all_losses = masked_loss.view(-1, num_classes)
        # expand mask_label to all_losses
        rel_mask = rel_mask.unsqueeze(-1).expand_as(all_losses)
        
        # Assign weights based on the true labels
        weight_c = labels_one_hot * self.positive_weight + (1 - labels_one_hot) * self.negative_weight

        # apply mask
        all_losses = all_losses * rel_mask.float() * weight_c
        rel_loss = all_losses.sum()
        total_loss = rel_loss

        if hasattr(self, "coref_classifier"):
            if coref_mask.sum() == 0:
                logger.info("Coreference mask is empty, skipping coreference loss calculation")
            else:
                # compute coreference loss (masked for coreference labels only)
                coref_scores = coref_scores.view(-1)                                # Flatten coref_scores to match label shape (B * num_pairs * 1)

                # Prepare coref_ground_truth with valid target values (i.e, set -2 -> 1 and others -> 0)
                coref_ground_truth = torch.zeros_like(labels, dtype=torch.float32)
                coref_ground_truth[coref_mask] = 1.0

                valid_mask = (labels != -1)

                coref_loss = self.compute_coref_loss(coref_scores[valid_mask], coref_ground_truth[valid_mask])
                coref_loss = self.config.coref_loss_weight * coref_loss
                total_loss += coref_loss
                return {'total_loss': total_loss, 'coref_loss': coref_loss, 'rel_loss': rel_loss}

        return {'total_loss': total_loss} # total_loss is rel_loss if no coref_classifier
    

    @torch.no_grad()
    def predict(self, x, flat_ner=False, threshold: list | float = 0.5, ner=None):
        self.eval()
        
        # start_time = time.time()
        
        local_scores, num_classes, rel_type_mask, coref_scores = self.compute_score(x)
        
        # forward_pass_time = time.time() - start_time
        # logger.info(f"[Optimized Predict] Time taken for forward pass: {forward_pass_time:.4f} seconds")

        if isinstance(threshold, float):
            threshold = [threshold]
        
        probabilities = torch.sigmoid(local_scores)  # Shape: [batch_size, num_pairs, num_classes]
        
        # Start timing thresholding without synchronization
        # start = time.time()
        
        # Build a global mapping from class names to IDs
        all_class_names = set()
        for classes in x['classes_to_id']:
            all_class_names.update(classes.keys())
        class_name_to_id = {name: idx for idx, name in enumerate(sorted(all_class_names))}
        id_to_class_name = {idx: name for name, idx in class_name_to_id.items()}
        num_classes_total = len(class_name_to_id)

        # Convert types_list to tensors of class IDs
        types_list = [torch.tensor([class_name_to_id[name] for name in classes.keys()], device=probabilities.device) for classes in x['classes_to_id']]
        max_num_classes = max(len(types) for types in types_list)
        padded_types_tensor = torch.full((len(types_list), max_num_classes), -1, dtype=torch.long, device=probabilities.device)
        for idx, types in enumerate(types_list):
            padded_types_tensor[idx, :types.size(0)] = types

        # Convert x['relations_idx'] to a padded tensor
        relations_idx_list = x['relations_idx']
        max_num_pairs = probabilities.shape[1]  # Should match num_pairs in local_scores
        # Determine the maximum shape beyond the first dimension
        max_relations_idx_shape = relations_idx_list[0].shape[1:]  # Exclude the first dimension (num_pairs)

        # Initialize the padded tensor with the maximum shape
        padded_shape = (len(relations_idx_list), max_num_pairs) + max_relations_idx_shape
        padded_relations_idx = torch.full(padded_shape, -1, dtype=torch.long, device=probabilities.device)

        # Pad and assign each relations_idx tensor
        for idx, relations_idx in enumerate(relations_idx_list):
            num_pairs = relations_idx.shape[0]
            padded_relations_idx[idx, :num_pairs, ...] = relations_idx.to(probabilities.device)

        # logger.info(f"## Max Number of entity pairs: {max_num_pairs}")
        # logger.info(f"## Max Number of classes: {max_num_classes}")

        # Initialize the dictionary to store results per threshold
        rels_per_threshold = {}
        for thresh in threshold:
            # Apply threshold
            triggered_relations = probabilities > thresh  # Shape: [batch_size, num_pairs, num_classes]

            # Build a mask for valid class indices
            batch_sizes = torch.tensor([len(types) for types in types_list], device=probabilities.device)
            class_mask = torch.arange(max_num_classes, device=probabilities.device).unsqueeze(0).unsqueeze(0) < batch_sizes.unsqueeze(1).unsqueeze(2)
            triggered_relations &= class_mask

            # Get indices where relations are triggered
            batch_indices, pair_indices, class_indices = torch.nonzero(triggered_relations, as_tuple=True)

            if batch_indices.numel() == 0:
                rels = [[] for _ in range(len(x["tokens"]))]
                rels_per_threshold[thresh] = rels
                continue

            # Get scores
            scores = probabilities[batch_indices, pair_indices, class_indices]
            
            # Map class indices to actual class IDs
            class_ids = padded_types_tensor[batch_indices, class_indices]
            
            # Remove invalid class IDs (i.e., where class_id == -1)
            valid_class_mask = class_ids != -1
            batch_indices = batch_indices[valid_class_mask]
            pair_indices = pair_indices[valid_class_mask]
            class_ids = class_ids[valid_class_mask]
            scores = scores[valid_class_mask]

            if batch_indices.numel() == 0:
                rels = [[] for _ in range(len(x["tokens"]))]
                rels_per_threshold[thresh] = rels
                continue

            # Get corresponding entity pairs
            entity_pairs = padded_relations_idx[batch_indices, pair_indices]  # Shape: [num_relations, ...]

            # Build a mask for valid entity pairs (entity_pair does not contain -1)
            valid_entity_mask = (entity_pairs != -1).all(dim=tuple(range(1, entity_pairs.dim())))
            batch_indices = batch_indices[valid_entity_mask]
            pair_indices = pair_indices[valid_entity_mask]
            entity_pairs = entity_pairs[valid_entity_mask]
            class_ids = class_ids[valid_entity_mask]
            scores = scores[valid_entity_mask]

            if batch_indices.numel() == 0:
                rels = [[] for _ in range(len(x["tokens"]))]
                rels_per_threshold[thresh] = rels
                continue

            # Convert class IDs to class names
            class_ids_cpu = class_ids.cpu()
            relation_types = [id_to_class_name[class_id.item()] for class_id in class_ids_cpu]

            # Collect relations per example
            rels = [[] for _ in range(len(x["tokens"]))]
            batch_indices_cpu = batch_indices.cpu()
            entity_pairs_cpu = entity_pairs.cpu()
            scores_cpu = scores.cpu()
            for idx in range(batch_indices.size(0)):
                i = batch_indices_cpu[idx].item()
                entity_pair = entity_pairs_cpu[idx].tolist()
                relation_type = relation_types[idx]
                score = scores_cpu[idx].item()
                rels[i].append((entity_pair, relation_type, score))

            rels_per_threshold[thresh] = rels


        # thresholding_time = time.time() - start
        # logger.info(f"[Optimized Predict] Time taken for thresholding: {thresholding_time:.4f} seconds")
        
        return rels_per_threshold if len(threshold) > 1 else rels_per_threshold[threshold[0]]



    def predict_relations(self, text, labels, flat_ner=True, threshold=0.5, ner=None, top_k=-1):
        return self.batch_predict_relations([text], labels, flat_ner=flat_ner, threshold=threshold, ner=[ner], top_k=top_k)[0]

    def batch_predict_relations(self, texts, labels, flat_ner=True, threshold=0.5, ner=None, top_k=-1):
        """
        Predict relations for a batch of texts.
        texts:  List of texts | List[str]
        labels: List of labels | List[str]
        ...
        """

        all_tokens = []
        all_start_token_idx_to_text_idx = []
        all_end_token_idx_to_text_idx = []

        for text in texts:
            tokens = []
            start_token_idx_to_text_idx = []
            end_token_idx_to_text_idx = []
            if type(text) is str:
                for match in re.finditer(r'\w+(?:[-_]\w+)*|\S', text):
                    tokens.append(match.group())
                    start_token_idx_to_text_idx.append(match.start())
                    end_token_idx_to_text_idx.append(match.end())
            else:
                tokens = text  # already tokenized
            all_tokens.append(tokens)
            all_start_token_idx_to_text_idx.append(start_token_idx_to_text_idx)
            all_end_token_idx_to_text_idx.append(end_token_idx_to_text_idx)

*Content truncated for brevity.*

```

## File: glirel/test_spacy_integration.py

<a name='file-glirel-test_spacy_integration.py'></a>
*Description*: This is a Python script.

```python
import pytest
import spacy
from unittest.mock import patch, MagicMock

@pytest.fixture
def setup_nlp():
    # Load spaCy pipeline and add GLiREL component
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe(
        "glirel", 
        after="ner",
        config={"model": "jackboyla/glirel-large-v0", "batch_size": 1, "threshold": 0.0}
    )
    return nlp

def test_glirel_pipeline(setup_nlp):
    text = (
        "Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in April 1976. "
        "The company is headquartered in Cupertino, California."
    )
    labels = {
        "glirel_labels": {
            "co-founder": {"allowed_head": ["PERSON"], "allowed_tail": ["ORG"]},
            "headquartered in": {"allowed_head": ["ORG"], "allowed_tail": ["LOC", "GPE", "FAC"]},
        }
    }

    # Run pipeline
    docs = list(setup_nlp.pipe([(text, labels)], as_tuples=True))
    doc, context = docs[0]

    # Check relations in the output
    assert hasattr(doc._, 'relations'), "Expected relations attribute in the output."
    relations = doc._.relations
    assert len(relations) > 0, "Expected > 0 relations in the output."


```

## File: glirel/spacy_integration.py

<a name='file-glirel-spacy_integration.py'></a>
*Description*: This is a Python script.

```python
import os
import types
from typing import List, Optional, Union, Dict

import torch
from datasets import Dataset
from spacy.tokens import Doc, Span
from spacy.util import filter_spans, minibatch
from loguru import logger

from glirel import GLiREL
from glirel.modules.utils import constrain_relations_by_entity_type


class SpacyGLiRELWrapper:
    """This wrapper allows GLiREL to be easily used as a spaCy pipeline component.

    Usage:

        # Add the GLiREL component to the pipeline
        >>> nlp.add_pipe("glirel", after="ner")

        # Now you can use the pipeline with the GLiREL component
        >>> text = "Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in April 1976. The company is headquartered in Cupertino, California."

        >>> labels = {"glirel_labels": {
            'co-founder': {"allowed_head": ["PERSON"], "allowed_tail": ["ORG"]}, 
            'country of origin': {"allowed_head": ["PERSON", "ORG"], "allowed_tail": ["LOC", "GPE"]}, 
            'licensed to broadcast to': {"allowed_head": ["ORG"]},  
            'no relation': {},  
            'parent': {"allowed_head": ["PERSON"], "allowed_tail": ["PERSON"]}, 
            'followed by': {"allowed_head": ["PERSON", "ORG"], "allowed_tail": ["PERSON", "ORG"]},  
            'located in or next to body of water': {"allowed_head": ["LOC", "GPE", "FAC"], "allowed_tail": ["LOC", "GPE"]},  
            'spouse': {"allowed_head": ["PERSON"], "allowed_tail": ["PERSON"]},  
            'child': {"allowed_head": ["PERSON"], "allowed_tail": ["PERSON"]},  
            'founder': {"allowed_head": ["PERSON"], "allowed_tail": ["ORG"]},  
            'founded on date': {"allowed_head": ["ORG"], "allowed_tail": ["DATE"]},
            'headquartered in': {"allowed_head": ["ORG"], "allowed_tail": ["LOC", "GPE", "FAC"]},  
            'acquired by': {"allowed_head": ["ORG"], "allowed_tail": ["ORG", "PERSON"]},  
            'subsidiary of': {"allowed_head": ["ORG"], "allowed_tail": ["ORG", "PERSON"]}, 
            }
        }

        >>> docs = list( nlp.pipe([(text, labels)], as_tuples=True) )
        >>> relations = docs[0][0]._.relations

        >>> sorted_data_desc = sorted(relations, key=lambda x: x['score'], reverse=True)
        >>> print("\nDescending Order by Score:")
        >>> for item in sorted_data_desc:
            print(item)

        >>> Descending Order by Score:
        {'head_pos': [0, 2], 'tail_pos': [25, 26], 'head_text': ['Apple', 'Inc.'], 'tail_text': ['California'], 'label': 'headquartered in', 'score': 0.9854260683059692}
        {'head_pos': [0, 2], 'tail_pos': [23, 24], 'head_text': ['Apple', 'Inc.'], 'tail_text': ['Cupertino'], 'label': 'headquartered in', 'score': 0.9569844603538513}
        {'head_pos': [8, 10], 'tail_pos': [0, 2], 'head_text': ['Steve', 'Wozniak'], 'tail_text': ['Apple', 'Inc.'], 'label': 'co-founder', 'score': 0.09025496244430542}
        {'head_pos': [5, 7], 'tail_pos': [0, 2], 'head_text': ['Steve', 'Jobs'], 'tail_text': ['Apple', 'Inc.'], 'label': 'co-founder', 'score': 0.08805803954601288}
        {'head_pos': [12, 14], 'tail_pos': [0, 2], 'head_text': ['Ronald', 'Wayne'], 'tail_text': ['Apple', 'Inc.'], 'label': 'co-founder', 'score': 0.07996643334627151}

    """

    def __init__(
        self,
        pretrained_model_name_or_path: Union[str, os.PathLike],
        *args,
        batch_size: int = 1,
        device: Optional[Union[str, torch.device]] = None,
        threshold: float = 0.3,
        **kwargs,
    ) -> None:
        """Initialize a SpanMarker wrapper for spaCy.

        Args:
            pretrained_model_name_or_path (Union[str, os.PathLike]): The path to a locally pretrained SpanMarker model
                or a model name from the Hugging Face hub, e.g. `tomaarsen/span-marker-roberta-large-ontonotes5`
            batch_size (int): The number of samples to include per batch. Higher is faster, but requires more memory.
                Defaults to 4.
            device (Optional[Union[str, torch.device]]): The device to place the model on. Defaults to None.
            overwrite_entities (bool): Whether to overwrite the existing entities in the `doc.ents` attribute.
                Defaults to False.
        """
        self.model = GLiREL.from_pretrained(pretrained_model_name_or_path, *args, **kwargs)
        if device:
            self.model.to(device)
        elif torch.cuda.is_available():
            self.model.to("cuda")
        self.batch_size = batch_size
        self.threshold = threshold

    def _set_relatons(self, doc: Doc, relations: List[Dict]):
        doc.set_extension("relations", default=None, force=True)
        doc._.relations = relations
        return doc

    def __call__(self, doc: Doc, threshold=None) -> Doc:
        threshold = threshold or self.threshold
        if len(doc.ents) < 2: 
            logger.warning("The input text must contain at least two entities; skipping...")
            doc = self._set_relatons(doc, relations=[])
            return doc

        try:
            labels = doc._context["glirel_labels"]
        except Exception as e:
            logger.error("The labels must be passed as a context attribute eg, `nlp.pipe([(text, {'re_labels': ['father', ..]})], as_tuples=True)`")
            raise e

        if isinstance(labels, dict):
            labels_and_constraints = labels
            labels = list(labels.keys())
        
        tokens = [token.text for token in doc]
        ner = [[ent.start, (ent.end - 1), ent.label_, ent.text] for ent in doc.ents]
        relations = self.model.predict_relations(tokens, labels, threshold=threshold, ner=ner, top_k=1)

        if isinstance(doc._context["glirel_labels"], list) is False:
            relations = constrain_relations_by_entity_type(doc.ents, labels_and_constraints, relations)

        doc = self._set_relatons(doc, relations)
        return doc

    # def pipe(self, stream, batch_size=128):
    #     ...
```

## File: glirel/modules/evaluator.py

<a name='file-glirel-modules-evaluator.py'></a>
*Description*: This is a Python script.

```python
from collections import defaultdict

import numpy as np
import os
import json
import torch
from seqeval.metrics.v1 import _prf_divide


class RelEvaluator:
    def __init__(self, all_true, all_outs, dataset_name: str = None):
        self.all_true = all_true
        self.all_outs = all_outs
        self.dataset_name = dataset_name

    def get_relations_fr(self, rels):
        all_rels = []
        for r in rels:
            all_rels.append(
                [
                    r['relation_text'], 
                    tuple(r['head']['position']), 
                    tuple(r['tail']['position'])
                ]
            )
        return all_rels

    def transform_data(self):
        all_true_rel = []
        all_outs_rel = []
        for i, j in zip(self.all_true, self.all_outs):
            e = self.get_relations_fr(i)
            all_true_rel.append(e)
            e = self.get_relations_fr(j)
            all_outs_rel.append(e)
        
        # # DEBUG: find all the relations we missed or got wrong
        # for i, (true, pred) in enumerate(zip(all_true_rel, all_outs_rel)):
        #     instance_all_true_set = set([tuple(t) for t in true])
        #     instance_out_set = set([tuple(t) for t in pred])
        #     assert len(instance_all_true_set) == len(true), f"Duplicate relations in true data for instance {i}"
        #     assert len(instance_out_set) == len(pred), f"Duplicate relations in predicted data for instance {i}"
        #     fn, tp, fp = [], [], []
        #     for p in instance_out_set:
        #         if p in instance_all_true_set:
        #             tp.append(p)
        #         else:
        #             fp.append(p)
        #     for t in instance_all_true_set:
        #         if t not in instance_out_set:
        #             fn.append(t)
        #     import ipdb; ipdb.set_trace()
                
        return all_true_rel, all_outs_rel

    @torch.no_grad()
    def evaluate(self):
        all_true_typed, all_outs_typed = self.transform_data()
        micro_precision, micro_recall, micro_f1, macro_precision, macro_recall, macro_f1 = self.compute_prf(all_true_typed, all_outs_typed).values()
        output_str = f"Micro P: {micro_precision:.2%}\tMicro R: {micro_recall:.2%}\tMicro F1: {micro_f1:.2%}\n"
        output_str += f"Macro P: {macro_precision:.2%}\tMacro R: {macro_recall:.2%}\tMacro F1: {macro_f1:.2%}\n"
        metric_dict = {
            "micro_precision": micro_precision,
            "micro_recall": micro_recall,
            "micro_f1": micro_f1,
            "macro_precision": macro_precision,
            "macro_recall": macro_recall,
            "macro_f1": macro_f1,
        }
        return output_str, metric_dict
    
    def extract_tp_actual_correct(self, y_true, y_pred):
        # y_pred[0] -> ['work location', (19, 20), (23, 24), 0]
        relations_true = defaultdict(set)
        relations_pred = defaultdict(set)

        for type_name, head, tail, idx in y_true:
            relations_true[type_name].add((head, tail, idx))
        for type_name, head, tail, idx in y_pred:
            # NOTE: we are only interested in the evaluating against 
            # annotated relations that are present in the true data (i.e. not the ones that are not annotated in the case of FewRel)
            if self.dataset_name in ["few_rel", "wiki_zsl", "redocred"]:
                if any((head, tail, idx) in relations_true[t] for t in relations_true.keys()):
                    relations_pred[type_name].add((head, tail, idx))
            else:
                relations_pred[type_name].add((head, tail, idx))


        target_names = sorted(set(relations_true.keys()) | set(relations_pred.keys()))

        tp_sum = np.array([], dtype=np.int32)
        pred_sum = np.array([], dtype=np.int32)
        true_sum = np.array([], dtype=np.int32)
        for type_name in target_names:
            relations_true_type = relations_true.get(type_name, set())
            relations_pred_type = relations_pred.get(type_name, set())
            tp_sum = np.append(tp_sum, len(relations_true_type & relations_pred_type))
            pred_sum = np.append(pred_sum, len(relations_pred_type))
            true_sum = np.append(true_sum, len(relations_true_type))

        return pred_sum, tp_sum, true_sum, target_names

    def flatten_for_eval(self, y_true, y_pred):
        all_true = []
        all_pred = []

        for i, (true, pred) in enumerate(zip(y_true, y_pred)):
            all_true.extend([t + [i] for t in true])
            all_pred.extend([p + [i] for p in pred])

        return all_true, all_pred


    def compute_prf(self, y_true, y_pred):
        # macro will weight all classes equally, micro will weight all instances equally (regardless of class)
        # ref (because I always forget) -> https://datascience.stackexchange.com/a/24051
        y_true, y_pred = self.flatten_for_eval(y_true, y_pred)

        pred_sum, tp_sum, true_sum, target_names = self.extract_tp_actual_correct(y_true, y_pred)

            
        # Macro averaging calculates the metrics for each class separately and then average them
        macro_f_score, macro_recall, macro_precision = [], [], []
        for i in range(len(tp_sum)):
            p = _prf_divide(numerator=np.array([tp_sum[i]]), denominator=np.array([pred_sum[i]]), metric='precision', modifier='predicted', average='macro', warn_for=('precision',), zero_division='warn')
            r = _prf_divide(numerator=np.array([tp_sum[i]]), denominator=np.array([true_sum[i]]), metric='recall', modifier='true', average='macro', warn_for=('recall',), zero_division='warn')
            f = 2 * (p * r) / (p + r) if p + r != 0 else np.array([0])
            macro_precision.append(p)
            macro_recall.append(r)
            macro_f_score.append(f)
        macro_precision = [np.mean(macro_precision)]
        macro_recall = [np.mean(macro_recall)]
        macro_f_score = [np.mean(macro_f_score)]


        # Micro averaging is simply the total number of true positives, false positives, and false negatives
        tp_sum = np.array([tp_sum.sum()])
        pred_sum = np.array([pred_sum.sum()])
        true_sum = np.array([true_sum.sum()])

        micro_precision = _prf_divide(
            numerator=tp_sum,
            denominator=pred_sum,
            metric='precision',
            modifier='predicted',
            average='micro',
            warn_for=('precision', 'recall', 'f-score'),
            zero_division='warn'
        )

        micro_recall = _prf_divide(
            numerator=tp_sum,
            denominator=true_sum,
            metric='recall',
            modifier='true',
            average='micro',
            warn_for=('precision', 'recall', 'f-score'),
            zero_division='warn'
        )

        denominator = micro_precision + micro_recall
        denominator[denominator == 0.] = 1
        micro_f_score = 2 * (micro_precision * micro_recall) / denominator


        return {'micro_precision': micro_precision[0], 'micro_recall': micro_recall[0], 'micro_f_score': micro_f_score[0],
                'macro_precision': macro_precision[0], 'macro_recall': macro_recall[0], 'macro_f_score': macro_f_score[0],
                }



def is_nested(idx1, idx2):
    # Return True if idx2 is nested inside idx1 or vice versa
    return (idx1[0] <= idx2[0] and idx1[1] >= idx2[1]) or (idx2[0] <= idx1[0] and idx2[1] >= idx1[1])


def has_overlapping(idx1, idx2):
    overlapping = True
    if idx1[:2] == idx2[:2]:
        return overlapping
    if (idx1[0] > idx2[1] or idx2[0] > idx1[1]):
        overlapping = False
    return overlapping


def has_overlapping_nested(idx1, idx2):
    # Return True if idx1 and idx2 overlap, but neither is nested inside the other
    if idx1[:2] == idx2[:2]:
        return True
    if ((idx1[0] > idx2[1] or idx2[0] > idx1[1]) or is_nested(idx1, idx2)) and idx1 != idx2:
        return False
    else:
        return True


def greedy_search(spans, flat_ner=True):  # start, end, class, score

    if flat_ner:
        has_ov = has_overlapping
    else:
        has_ov = has_overlapping_nested

    new_list = []
    span_prob = sorted(spans, key=lambda x: -x[-1])
    for i in range(len(spans)):
        b = span_prob[i]
        flag = False
        for new in new_list:
            if has_ov(b[:-1], new):
                flag = True
                break
        if not flag:
            new_list.append(b[:-1])
    new_list = sorted(new_list, key=lambda x: x[0])
    return new_list

```

## File: glirel/modules/token_rep.py

<a name='file-glirel-modules-token_rep.py'></a>
*Description*: This is a Python script.

```python
from typing import List

import torch
from flair.data import Sentence
from flair.embeddings import TransformerWordEmbeddings
from torch import nn
from torch.nn.utils.rnn import pad_sequence


# flair.cache_root = '/gpfswork/rech/pds/upa43yu/.cache'


class TokenRepLayer(nn.Module):
    def __init__(self, model_name: str, fine_tune: bool, subtoken_pooling: str,
                 hidden_size: int,
                 add_tokens: List[str]
                 ):
        super().__init__()

        self.bert_layer = TransformerWordEmbeddings(
            model_name,
            fine_tune=fine_tune,
            subtoken_pooling=subtoken_pooling,
            allow_long_sentences=True
        )

        # add tokens to vocabulary
        self.bert_layer.tokenizer.add_tokens(add_tokens)

        # resize token embeddings
        self.bert_layer.model.resize_token_embeddings(len(self.bert_layer.tokenizer))

        bert_hidden_size = self.bert_layer.embedding_length

        if hidden_size != bert_hidden_size:
            self.projection = nn.Linear(bert_hidden_size, hidden_size)

    def forward(self, tokens: List[List[str]], lengths: torch.Tensor):
        token_embeddings = self.compute_word_embedding(tokens)

        if hasattr(self, "projection"):
            token_embeddings = self.projection(token_embeddings)

        B = len(lengths)
        max_length = lengths.max()
        mask = (torch.arange(max_length).view(1, -1).repeat(B, 1) < lengths.cpu().unsqueeze(1)).to(
            token_embeddings.device).long()
        return {"embeddings": token_embeddings, "mask": mask}

    def compute_word_embedding(self, tokens):
        sentences = [Sentence(i) for i in tokens]
        """
        sentences[0]
            Sentence[29]: "[REL] doctoral advisor [REL] publisher [REL] connecting line [SEP] The Church of the Faroe Islands ( Faroese Fólkakirkjan ) is one of the smallest of the worlds state church es ."
        [t for t in sentences[0].tokens]
            [Token[0]: "[REL]", Token[1]: "doctoral advisor", Token[2]: "[REL]", Token[3]: "publisher", Token[4]: "[REL]", Token[5]: "connecting line", Token[6]: "[SEP]", Token[7]: "The", Token[8]: "Church", Token[9]: "of", Token[10]: "the", Token[11]: "Faroe", Token[12]: "Islands", Token[13]: "(", Token[14]: "Faroese", Token[15]: "Fólkakirkjan", Token[16]: ")", Token[17]: "is", Token[18]: "one", Token[19]: "of", Token[20]: "the", Token[21]: "smallest", Token[22]: "of", Token[23]: "the", Token[24]: "worlds", Token[25]: "state", Token[26]: "church", Token[27]: "es", Token[28]: "."]
        """
        self.bert_layer.embed(sentences)
        token_embeddings = pad_sequence([torch.stack([t.embedding for t in k]) for k in sentences], batch_first=True)
        return token_embeddings

```

## File: glirel/modules/loss_functions.py

<a name='file-glirel-modules-loss_functions.py'></a>
*Description*: This is a Python script.

```python
import torch
import torch.nn.functional as F


def focal_loss_with_logits(
        inputs: torch.Tensor,
        targets: torch.Tensor,
        alpha: float = 0.25,
        gamma: float = 2,
        reduction: str = "none",
) -> torch.Tensor:
    """
    Loss used in RetinaNet for dense detection: https://arxiv.org/abs/1708.02002.

    Args:
        inputs (Tensor): A float tensor of arbitrary shape.
                The predictions for each example.
        targets (Tensor): A float tensor with the same shape as inputs. Stores the binary
                classification label for each element in inputs
                (0 for the negative class and 1 for the positive class).
        alpha (float): Weighting factor in range (0,1) to balance
                positive vs negative examples or -1 for ignore. Default: ``0.25``.
        gamma (float): Exponent of the modulating factor (1 - p_t) to
                balance easy vs hard examples. Default: ``2``.
        reduction (string): ``'none'`` | ``'mean'`` | ``'sum'``
                ``'none'``: No reduction will be applied to the output.
                ``'mean'``: The output will be averaged.
                ``'sum'``: The output will be summed. Default: ``'none'``.
    Returns:
        Loss tensor with the reduction option applied.
    """
    # Original implementation from https://github.com/facebookresearch/fvcore/blob/master/fvcore/nn/focal_loss.py

    p = torch.sigmoid(inputs)
    loss = F.binary_cross_entropy_with_logits(inputs, targets, reduction="none")
    if gamma > 0:
        p_t = p * targets + (1 - p) * (1 - targets)
        loss = loss * ((1 - p_t) ** gamma)

    if alpha >= 0:
        alpha_t = alpha * targets + (1 - alpha) * (1 - targets)
        loss = alpha_t * loss

    # Check reduction option and return loss accordingly
    if reduction == "none":
        pass
    elif reduction == "mean":
        loss = loss.mean()
    elif reduction == "sum":
        loss = loss.sum()
    else:
        raise ValueError(
            f"Invalid Value for arg 'reduction': '{reduction} \n Supported reduction modes: 'none', 'mean', 'sum'"
        )
    return loss
```

## File: glirel/modules/span_rep.py

<a name='file-glirel-modules-span_rep.py'></a>
*Description*: This is a Python script.

```python
import torch
import torch.nn.functional as F
from torch import nn

def create_projection_layer(hidden_size: int, dropout: float, out_dim: int = None) -> nn.Sequential:
    """
    Creates a projection layer with specified configurations.
    """
    if out_dim is None:
        out_dim = hidden_size

    return nn.Sequential(
        nn.Linear(hidden_size, out_dim * 4),
        nn.ReLU(),
        nn.Dropout(dropout),
        nn.Linear(out_dim * 4, out_dim)
    )

def extract_elements(sequence, indices):
    B, L, D = sequence.shape
    K = indices.shape[1]

    # Expand indices to [B, K, D]
    expanded_indices = indices.unsqueeze(2).expand(-1, -1, D)

    # Gather the elements
    extracted_elements = torch.gather(sequence, 1, expanded_indices)

    return extracted_elements


class SpanMarkerV0(nn.Module):
    """
    Marks and projects span endpoints using an MLP.
    """

    def __init__(self, hidden_size: int, max_width: int, dropout: float = 0.4):
        super().__init__()
        self.max_width = max_width
        self.project_start = create_projection_layer(hidden_size, dropout)
        self.project_end = create_projection_layer(hidden_size, dropout)

        self.out_project = create_projection_layer(hidden_size * 2, dropout, hidden_size)

    def forward(self, h: torch.Tensor, span_idx: torch.Tensor) -> torch.Tensor:
        B, L, D = h.size()
        # span_idx.shape    ([B, num_possible_spans, 2])

        start_rep = self.project_start(h)  # ([B, L, D])
        end_rep = self.project_end(h)      # ([B, L, D])

        start_span_rep = extract_elements(start_rep, span_idx[:, :, 0])  # ([B, num_possible_spans, D])
        end_span_rep = extract_elements(end_rep, span_idx[:, :, 1])      # ([B, num_possible_spans, D])

        cat = torch.cat([start_span_rep, end_span_rep], dim=-1).relu()   # ([B, num_possible_spans, D*2])

        return self.out_project(cat).view(B, L, self.max_width, D)
    

class SpanQuery(nn.Module):

    def __init__(self, hidden_size, max_width, trainable=True):
        super().__init__()

        self.query_seg = nn.Parameter(torch.randn(hidden_size, max_width))

        nn.init.uniform_(self.query_seg, a=-1, b=1)

        if not trainable:
            self.query_seg.requires_grad = False

        self.project = nn.Sequential(
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU()
        )

    def forward(self, h, *args):
        # h of shape [B, L, D]
        # query_seg of shape [D, max_width]

        span_rep = torch.einsum('bld, ds->blsd', h, self.query_seg)

        return self.project(span_rep)


class SpanMLP(nn.Module):

    def __init__(self, hidden_size, max_width):
        super().__init__()

        self.mlp = nn.Linear(hidden_size, hidden_size * max_width)

    def forward(self, h, *args):
        # h of shape [B, L, D]
        # query_seg of shape [D, max_width]

        B, L, D = h.size()

        span_rep = self.mlp(h)

        span_rep = span_rep.view(B, L, -1, D)

        return span_rep.relu()


class SpanCAT(nn.Module):

    def __init__(self, hidden_size, max_width):
        super().__init__()

        self.max_width = max_width

        self.query_seg = nn.Parameter(torch.randn(128, max_width))

        self.project = nn.Sequential(
            nn.Linear(hidden_size + 128, hidden_size),
            nn.ReLU()
        )

    def forward(self, h, *args):
        # h of shape [B, L, D]
        # query_seg of shape [D, max_width]

        B, L, D = h.size()

        h = h.view(B, L, 1, D).repeat(1, 1, self.max_width, 1)

        q = self.query_seg.view(1, 1, self.max_width, -1).repeat(B, L, 1, 1)

        span_rep = torch.cat([h, q], dim=-1)

        span_rep = self.project(span_rep)

        return span_rep


class SpanConvBlock(nn.Module):
    def __init__(self, hidden_size, kernel_size, span_mode='conv_normal'):
        super().__init__()

        if span_mode == 'conv_conv':
            self.conv = nn.Conv1d(hidden_size, hidden_size,
                                  kernel_size=kernel_size)

            # initialize the weights
            nn.init.kaiming_uniform_(self.conv.weight, nonlinearity='relu')

        elif span_mode == 'conv_max':
            self.conv = nn.MaxPool1d(kernel_size=kernel_size, stride=1)
        elif span_mode == 'conv_mean' or span_mode == 'conv_sum':
            self.conv = nn.AvgPool1d(kernel_size=kernel_size, stride=1)

        self.span_mode = span_mode

        self.pad = kernel_size - 1

    def forward(self, x):

        x = torch.einsum('bld->bdl', x)

        if self.pad > 0:
            x = F.pad(x, (0, self.pad), "constant", 0)

        x = self.conv(x)

        if self.span_mode == "conv_sum":
            x = x * (self.pad + 1)

        return torch.einsum('bdl->bld', x)


class SpanConv(nn.Module):
    def __init__(self, hidden_size, max_width, span_mode):
        super().__init__()

        kernels = [i + 2 for i in range(max_width - 1)]

        self.convs = nn.ModuleList()

        for kernel in kernels:
            self.convs.append(SpanConvBlock(hidden_size, kernel, span_mode))

        self.project = nn.Sequential(
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size)
        )

    def forward(self, x, *args):

        span_reps = [x]

        for conv in self.convs:
            h = conv(x)
            span_reps.append(h)

        span_reps = torch.stack(span_reps, dim=-2)

        return self.project(span_reps)


class SpanEndpointsBlock(nn.Module):
    def __init__(self, kernel_size):
        super().__init__()

        self.kernel_size = kernel_size

    def forward(self, x):
        B, L, D = x.size()

        span_idx = torch.LongTensor(
            [[i, i + self.kernel_size - 1] for i in range(L)]).to(x.device)

        x = F.pad(x, (0, 0, 0, self.kernel_size - 1), "constant", 0)

        # endrep
        start_end_rep = torch.index_select(x, dim=1, index=span_idx.view(-1))

        start_end_rep = start_end_rep.view(B, L, 2, D)

        return start_end_rep


class ConvShare(nn.Module):
    def __init__(self, hidden_size, max_width):
        super().__init__()

        self.max_width = max_width

        self.conv_weigth = nn.Parameter(
            torch.randn(hidden_size, hidden_size, max_width))

        nn.init.kaiming_uniform_(self.conv_weigth, nonlinearity='relu')

        self.project = nn.Sequential(
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size)
        )

    def forward(self, x, *args):
        span_reps = []

        x = torch.einsum('bld->bdl', x)

        for i in range(self.max_width):
            pad = i
            x_i = F.pad(x, (0, pad), "constant", 0)
            conv_w = self.conv_weigth[:, :, :i + 1]
            out_i = F.conv1d(x_i, conv_w)
            span_reps.append(out_i.transpose(-1, -2))

        out = torch.stack(span_reps, dim=-2)

        return self.project(out)


class SpanMarker(nn.Module):

    def __init__(self, hidden_size, max_width, dropout=0.4):
        super().__init__()

        self.max_width = max_width

        self.project_start = nn.Sequential(
            nn.Linear(hidden_size, hidden_size * 2, bias=True),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size * 2, hidden_size, bias=True),
        )

        self.project_end = nn.Sequential(
            nn.Linear(hidden_size, hidden_size * 2, bias=True),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size * 2, hidden_size, bias=True),
        )

        self.out_project = nn.Linear(hidden_size * 2, hidden_size, bias=True)

    def forward(self, h, span_idx):
        # h of shape [B, L, D]
        # query_seg of shape [D, max_width]

        B, L, D = h.size()

        # project start and end
        start_rep = self.project_start(h)
        end_rep = self.project_end(h)

        start_span_rep = extract_elements(start_rep, span_idx[:, :, 0])
        end_span_rep = extract_elements(end_rep, span_idx[:, :, 1])

        # concat start and end
        cat = torch.cat([start_span_rep, end_span_rep], dim=-1).relu()

        # project
        cat = self.out_project(cat)

        # reshape
        return cat.view(B, L, self.max_width, D)


class ConvShareV2(nn.Module):
    def __init__(self, hidden_size, max_width):
        super().__init__()

        self.max_width = max_width

        self.conv_weigth = nn.Parameter(
            torch.randn(hidden_size, hidden_size, max_width)
        )

        nn.init.xavier_normal_(self.conv_weigth)

    def forward(self, x, *args):
        span_reps = []

        x = torch.einsum('bld->bdl', x)

        for i in range(self.max_width):
            pad = i
            x_i = F.pad(x, (0, pad), "constant", 0)
            conv_w = self.conv_weigth[:, :, :i + 1]
            out_i = F.conv1d(x_i, conv_w)
            span_reps.append(out_i.transpose(-1, -2))

        out = torch.stack(span_reps, dim=-2)

        return out


class SpanRepLayer(nn.Module):
    """
    Various span representation approaches
    """

    def __init__(self, hidden_size, max_width, span_mode, **kwargs):
        super().__init__()

        if span_mode == 'marker':
            self.span_rep_layer = SpanMarker(hidden_size, max_width, **kwargs)
        elif span_mode == 'markerV0':
            self.span_rep_layer = SpanMarkerV0(hidden_size, max_width, **kwargs)
        elif span_mode == 'query':
            self.span_rep_layer = SpanQuery(
                hidden_size, max_width, trainable=True)
        elif span_mode == 'mlp':
            self.span_rep_layer = SpanMLP(hidden_size, max_width)
        elif span_mode == 'cat':
            self.span_rep_layer = SpanCAT(hidden_size, max_width)
        elif span_mode == 'conv_conv':
            self.span_rep_layer = SpanConv(
                hidden_size, max_width, span_mode='conv_conv')
        elif span_mode == 'conv_max':
            self.span_rep_layer = SpanConv(
                hidden_size, max_width, span_mode='conv_max')
        elif span_mode == 'conv_mean':
            self.span_rep_layer = SpanConv(
                hidden_size, max_width, span_mode='conv_mean')
        elif span_mode == 'conv_sum':
            self.span_rep_layer = SpanConv(
                hidden_size, max_width, span_mode='conv_sum')
        elif span_mode == 'conv_share':
            self.span_rep_layer = ConvShare(hidden_size, max_width)
        else:
            raise ValueError(f'Unknown span mode {span_mode}')

    def forward(self, x, *args):

        return self.span_rep_layer(x, *args)

```

## File: glirel/modules/custom_tokenizers.py

<a name='file-glirel-modules-custom_tokenizers.py'></a>
*Description*: This is a Python script.

```python

# from https://github.com/urchade/GLiNER/blob/main/gliner/data_processing/tokenizer.py

import re


class TokenSplitterBase():
    def __init__(self):
        pass

    def __call__(self, text) -> (str, int, int):
        pass


class WhitespaceTokenSplitter(TokenSplitterBase):
    def __init__(self):
        self.whitespace_pattern = re.compile(r'\w+(?:[-_]\w+)*|\S')
    
    def __call__(self, text):
        for match in self.whitespace_pattern.finditer(text):
            yield match.group(), match.start(), match.end()


class SpaCyTokenSplitter(TokenSplitterBase):
    def __init__(self, lang=None):
        try:
            import spacy # noqa
        except ModuleNotFoundError as error:
            raise error.__class__(
                "Please install spacy with: `pip install spacy`"
            )
        if lang is None:
            lang = 'en'  # Default to English if no language is specified
        self.nlp = spacy.blank(lang)

    def __call__(self, text):
        doc = self.nlp(text)
        for token in doc:
            yield token.text, token.idx, token.idx + len(token.text)            


class MecabKoTokenSplitter(TokenSplitterBase):
    def __init__(self):
        try:
            import mecab  # noqa
        except ModuleNotFoundError as error:
            raise error.__class__(
                "Please install python-mecab-ko with: `pip install python-mecab-ko`"
            )
        self.tagger = mecab.MeCab()
    
    def __call__(self, text):
        tokens = self.tagger.morphs(text)

        last_idx = 0
        for morph in tokens:
            start_idx = text.find(morph, last_idx)
            end_idx = start_idx + len(morph)
            last_idx = end_idx
            yield morph, start_idx, end_idx

class JiebaTokenSplitter(TokenSplitterBase):
    def __init__(self):
        try:
            import jieba  # noqa
        except ModuleNotFoundError as error:
            raise error.__class__(
                "Please install jieba with: `pip install jieba`"
            )
        self.tagger = jieba
    
    def __call__(self, text):
        tokens = self.tagger.cut(text)
        last_idx = 0
        for token in tokens:
            start_idx = text.find(token, last_idx)
            end_idx = start_idx + len(token)
            last_idx = end_idx
            yield token, start_idx, end_idx

class HanLPTokenSplitter(TokenSplitterBase):
    def __init__(self, model_name="FINE_ELECTRA_SMALL_ZH"):
        try:
            import hanlp  # noqa
            import hanlp.pretrained
        except ModuleNotFoundError as error:
            raise error.__class__(
                "Please install hanlp with: `pip install hanlp`"
            )

        models = hanlp.pretrained.tok.ALL
        if model_name not in models:
            raise ValueError(f"HanLP: {model_name} is not available, choose between {models.keys()}")
        url = models[model_name]
        self.tagger = hanlp.load(url)
    
    def __call__(self, text):
        tokens = self.tagger(text)
        last_idx = 0
        for token in tokens:
            start_idx = text.find(token, last_idx)
            end_idx = start_idx + len(token)
            last_idx = end_idx
            yield token, start_idx, end_idx

class WordsSplitter(TokenSplitterBase):
    def __init__(self, splitter_type='whitespace'):
        if splitter_type=='whitespace':
            self.splitter = WhitespaceTokenSplitter()
        elif splitter_type == 'spacy':
            self.splitter = SpaCyTokenSplitter()
        elif splitter_type == 'mecab':
            self.splitter = MecabKoTokenSplitter()
        elif splitter_type == 'jieba':
            self.splitter = JiebaTokenSplitter()
        elif splitter_type == 'hanlp':
            self.splitter = HanLPTokenSplitter()    
        else:
            raise ValueError(f"{splitter_type} is not implemented, choose between 'whitespace', 'spacy', 'jieba', 'hanlp' and 'mecab'")
    
    def __call__(self, text):
        for token in self.splitter(text):
            yield token
```

## File: glirel/modules/utils.py

<a name='file-glirel-modules-utils.py'></a>
*Description*: This is a Python script.

```python
import numpy as np
import torch
import torch.nn.functional as F


def remove_duplicates(data):
    """
    - Check for and remove duplicate spans and relations in the data.
    """

    for i, item in enumerate(data):
        # Remove duplicate relations
        relation_pos = set()
        unique_relations = []
        for r in item['relations']:
            position_tuple = (tuple(r['head']['position']), tuple(r['tail']['position']))
            if position_tuple not in relation_pos:
                relation_pos.add(position_tuple)
                unique_relations.append(r)
            else:
                print(f"Duplicate relation removed in (idx {i}) Relation --> {r}")
        item['relations'] = unique_relations  # Update relations with unique list

        # Remove duplicate spans
        span_set = set()
        unique_spans = []
        for span in item['ner']:
            span_pos = (span[0], span[1])
            if span_pos not in span_set:
                span_set.add(span_pos)
                unique_spans.append(span)
            else:
                print(f"Duplicate span removed in (idx {i}) Span --> {span}")
        item['ner'] = unique_spans  # Update NER spans with unique list

    return data


def sanity_check_data(data):
    """
    - Check for duplicate spans and relations in the data.
    - Ensure that the relation positions are found in the NER spans.
    """

    for i, item in enumerate(data):
        relation_pos = set()
        for r in item['relations']:
            position_tuple = (tuple(r['head']['position']), tuple(r['tail']['position']))
            # duplicate relations
            assert position_tuple not in relation_pos, f"Duplicate position for relation in (idx {i}) Relation --> {r}"
            relation_pos.add(position_tuple)

        span_set = set()
        for span in item['ner']:
            span_pos = (span[0], span[1])
            # duplicate spans
            assert span_pos not in span_set, f"Duplicate span in (idx {i}) Span --> {span}"
            span_set.add(span_pos)


        for pos_tuple in relation_pos:
            for pos in pos_tuple:
                # relation position not found in NER spans
                assert pos in span_set, f"Relation position not found in NER spans in (idx {i}) Relation position --> {pos}"


def constrain_relations_by_entity_type(ents, labels, relations):
    '''
    relations: {'head_pos': [15, 17], 'tail_pos': [25, 26], 'head_text': ['April', '1976'], 'tail_text': ['California'], 'label': 'headquartered in', 'score': 0.9820516705513}
    labels: {'father': {'allowed_head': ['PERSON'], 'allowed_tail': ['PERSON']}}
    '''
    ner = {(ent.start, ent.end): ent.label_ for ent in ents}
    rel_types = list(labels.keys())
    constrained_relations = []
    for relation in relations:
        head_label = ner[(relation['head_pos'][0], relation['head_pos'][1])]
        tail_label = ner[(relation['tail_pos'][0], relation['tail_pos'][1])]
        if head_label in labels[relation['label']].get('allowed_head', rel_types) and tail_label in labels[relation['label']].get('allowed_tail', rel_types):
            constrained_relations.append(relation)
    
    return constrained_relations

def get_entity_position(entity):
    return tuple(entity["position"])
    
def get_coreference_clusters(relations_list_of_lists, coreference_label="SELF"):
    """
    Generates coreference clusters from relations based on "SELF" relationships.

    Parameters:
    - relations: List of List of relation dictionaries.

    Returns:
    - sorted_clusters: List of List of clusters, each cluster is a list of entity positions.
    - entity_to_cluster_idx: List of Dictionary mapping entity positions to cluster indices.
    """
    if isinstance(relations_list_of_lists[0], dict):
        relations_list_of_lists = [relations_list_of_lists]

    sorted_clusters_list, entity_to_cluster_idx_list = [], []
    for relations in relations_list_of_lists:
        # Collect all unique entities
        entities = set()
        for relation in relations:
            head_pos = get_entity_position(relation["head"]) if "head" in relation else tuple(relation["head_pos"])
            tail_pos = get_entity_position(relation["tail"]) if "tail" in relation else tuple(relation["tail_pos"])
            entities.add(head_pos)
            entities.add(tail_pos)

        # Initialize Union-Find structure
        parent = {entity: entity for entity in entities}

        def find(u):
            # Path compression
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu != pv:
                parent[pu] = pv

        # Union entities connected by "SELF" relationships
        for relation in relations:
            relation_is_coreference = (relation["relation_text"] == coreference_label) if "relation_text" in relation else (relation['label'] == coreference_label)
            if relation_is_coreference:
                head_pos = get_entity_position(relation["head"]) if "head" in relation else tuple(relation["head_pos"])
                tail_pos = get_entity_position(relation["tail"]) if "tail" in relation else tuple(relation["tail_pos"])
                union(head_pos, tail_pos)

        # Build clusters based on connected components
        clusters = {}
        for entity in entities:
            root = find(entity)
            clusters.setdefault(root, []).append(entity)

        # Sort clusters by the earliest mention position
        sorted_clusters = sorted(
            clusters.values(),
            key=lambda cluster: min(pos[0] for pos in cluster)
        )

        # Create a mapping from entity positions to cluster indices
        entity_to_cluster_idx = {}
        for idx, cluster_entities in enumerate(sorted_clusters):
            for entity in cluster_entities:
                entity_to_cluster_idx[entity] = idx

        sorted_clusters_list.append(sorted_clusters)
        entity_to_cluster_idx_list.append(entity_to_cluster_idx)

    return sorted_clusters_list, entity_to_cluster_idx_list 

def aggregate_cluster_relations(entity_to_cluster_idx_list, relations_list, coreference_label="SELF"):
    """
    Aggregates relations across clusters based on the given clusters and relations.

    Parameters:
    - clusters: List of clusters, each cluster is a list of entity positions.
    - entity_to_cluster_idx: Dictionary mapping entity positions to cluster indices.
    - relations: Original list of relation dictionaries.

    Returns:
    - cluster_relations: List of aggregated cluster-to-cluster relations.
    """
    if isinstance(relations_list[0], dict):
        relations_list = [relations_list]
    if isinstance(entity_to_cluster_idx_list, dict):
        entity_to_cluster_idx_list = [entity_to_cluster_idx_list]

    cluster_relations_list = []
    for entity_to_cluster_idx, relations in zip(entity_to_cluster_idx_list, relations_list):
        # Initialize a set to avoid duplicates
        seen_relations = set()
        cluster_relations = []

        for relation in relations:
            # Skip "SELF" relations as they are used for coreference clustering
            relation_is_coreference = (relation["relation_text"] == coreference_label) if "relation_text" in relation else (relation['label'] == coreference_label)
            if relation_is_coreference:
                continue

            head_pos = get_entity_position(relation["head"]) if "head" in relation else tuple(relation["head_pos"])
            tail_pos = get_entity_position(relation["tail"]) if "tail" in relation else tuple(relation["tail_pos"])
            try:
                h_idx = entity_to_cluster_idx[head_pos]
                t_idx = entity_to_cluster_idx[tail_pos]
            except:
                print("relation", relation)
                print("head_pos", head_pos)
                print("tail_pos", tail_pos)
                print("entity_to_cluster_idx", entity_to_cluster_idx)
                raise
            r_text = relation["relation_text"] if "relation_text" in relation else relation['label']

            # Create the aggregated relation
            aggregated_relation = {
                "h_idx": h_idx,
                "t_idx": t_idx,
                "r": r_text
            }

            # Include additional fields if available
            for field in ["title", "evidence"]:
                if field in relation:
                    aggregated_relation[field] = relation[field]

            # Avoid duplicate relations
            relation_key = (h_idx, t_idx, r_text)
            if relation_key not in seen_relations:
                seen_relations.add(relation_key)
                cluster_relations.append(aggregated_relation)

        cluster_relations = sorted(cluster_relations, key=lambda x: (x["h_idx"], x["t_idx"], x["r"]))
        cluster_relations_list.append(cluster_relations)
    
    return cluster_relations_list

# from EnriCo --> https://github.com/urchade/EnriCo/blob/main/modules/utils.py

def down_weight_loss(logits, y, sample_rate=0.1, is_logit=True):
    rate = 1 - sample_rate

    if is_logit:
        loss_func = F.cross_entropy
    else:
        loss_func = F.nll_loss

    loss_entity = loss_func(logits, y.masked_fill(y == 0, -1), ignore_index=-1, reduction='sum')
    loss_non_entity = loss_func(logits, y.masked_fill(y > 0, -1), ignore_index=-1, reduction='sum')

    return loss_entity + loss_non_entity * rate


def get_relations(x, rel_logits, topk_pair_idx, max_top_k, candidate_spans_idx, threshold=0.5, output_confidence=False):
    rel_prob = torch.sigmoid(rel_logits)  # B, N, C

    relations = [[] for i in range(len(rel_logits))]

    rel_no = (rel_prob > threshold).nonzero(as_tuple=True)

    for bt, pos, cls in zip(*rel_no):
        lb = x["id_to_classes"][cls.item() + 1]
        pair_idx_pred = topk_pair_idx[bt, pos].item()
        head, tail = np.unravel_index(pair_idx_pred, (max_top_k, max_top_k))
        head = tuple(candidate_spans_idx[bt, head].tolist())
        tail = tuple(candidate_spans_idx[bt, tail].tolist())

        confidence = rel_prob[bt, pos, cls].item()

        if output_confidence:
            relations[bt.item()].append((head, tail, lb, confidence))
        else:
            relations[bt.item()].append((head, tail, lb))

    return relations


def get_relation_with_span(x):
    entities, relations = x['entities'], x['relations']
    B = len(entities)
    relation_with_span = [[] for i in range(B)]
    for i in range(B):
        rel_i = relations[i]
        ent_i = entities[i]
        for rel in rel_i:
            act = (ent_i[rel[0]], ent_i[rel[1]], rel[2])
            relation_with_span[i].append(act)
    return relation_with_span


def get_ground_truth_relations(x, candidate_spans_idx, candidate_span_label):
    B, max_top_k = candidate_span_label.shape

    relation_classes = torch.zeros((B, max_top_k, max_top_k), dtype=torch.long, device=candidate_spans_idx.device)

    # Populate relation classes
    for i in range(B):
        rel_i = x["relations"][i]
        ent_i = x["entities"][i]

        new_heads, new_tails, new_rel_type = [], [], []

        # Loop over the relations and entities to populate initial lists
        for k in rel_i:
            heads_i = [ent_i[k[0]][0], ent_i[k[0]][1]]
            tails_i = [ent_i[k[1]][0], ent_i[k[1]][1]]
            type_i = k[2]
            new_heads.append(heads_i)
            new_tails.append(tails_i)
            new_rel_type.append(type_i)

        # Update the original lists
        heads_, tails_, rel_type = new_heads, new_tails, new_rel_type

        # idx of candidate spans
        cand_i = candidate_spans_idx[i].tolist()

        for heads_i, tails_i, type_i in zip(heads_, tails_, rel_type):

            flag = False
            if isinstance(x["classes_to_id"], dict):
                if type_i in x["classes_to_id"]:
                    flag = True
            elif isinstance(x["classes_to_id"], list):
                if type_i in x["classes_to_id"][i]:
                    flag = True

            if heads_i in cand_i and tails_i in cand_i and flag:
                idx_head = cand_i.index(heads_i)
                idx_tail = cand_i.index(tails_i)

                if isinstance(x["classes_to_id"], list):
                    relation_classes[i, idx_head, idx_tail] = x["classes_to_id"][i][type_i]
                elif isinstance(x["classes_to_id"], dict):
                    relation_classes[i, idx_head, idx_tail] = x["classes_to_id"][type_i]

    # flat relation classes
    relation_classes = relation_classes.view(-1, max_top_k * max_top_k)

    # put to -1 class where corresponding candidate_span_label is -1 (for both head and tail)
    head_candidate_span_label = candidate_span_label.view(B, max_top_k, 1).repeat(1, 1, max_top_k).view(B, -1)
    tail_candidate_span_label = candidate_span_label.view(B, 1, max_top_k).repeat(1, max_top_k, 1).view(B, -1)

    relation_classes.masked_fill_(head_candidate_span_label.view(B, max_top_k * max_top_k) == -1, -1)  # head
    relation_classes.masked_fill_(tail_candidate_span_label.view(B, max_top_k * max_top_k) == -1, -1)  # tail

    return relation_classes


def _get_candidates(sorted_idx, tensor_elem, topk=10):
    # sorted_idx [B, num_spans]
    # tensor_elem [B, num_spans, D] or [B, num_spans]

    sorted_topk_idx = sorted_idx[:, :topk]

    if len(tensor_elem.shape) == 3:
        B, num_spans, D = tensor_elem.shape
        # [B, topk, D]
        topk_tensor_elem = tensor_elem.gather(1, sorted_topk_idx.unsqueeze(-1).expand(-1, -1, D))
    else:
        B, num_spans = tensor_elem.shape
        # [B, topk]
        topk_tensor_elem = tensor_elem.gather(1, sorted_topk_idx)

    return topk_tensor_elem, sorted_topk_idx
```

## File: glirel/modules/run_evaluation.py

<a name='file-glirel-modules-run_evaluation.py'></a>
*Description*: This is a Python script.

```python
import glob
import json
import os
import os

import torch
from tqdm import tqdm
import random


def open_content(path):
    paths = glob.glob(os.path.join(path, "*.json"))
    train, dev, test, labels = None, None, None, None
    for p in paths:
        if "train" in p:
            with open(p, "r") as f:
                train = json.load(f)
        elif "dev" in p:
            with open(p, "r") as f:
                dev = json.load(f)
        elif "test" in p:
            with open(p, "r") as f:
                test = json.load(f)
        elif "labels" in p:
            with open(p, "r") as f:
                labels = json.load(f)
    return train, dev, test, labels


def process(data):
    words = data['sentence'].split()
    entities = []  # List of entities (start, end, type)

    for entity in data['entities']:
        start_char, end_char = entity['pos']

        # Initialize variables to keep track of word positions
        start_word = None
        end_word = None

        # Iterate through words and find the word positions
        char_count = 0
        for i, word in enumerate(words):
            word_length = len(word)
            if char_count == start_char:
                start_word = i
            if char_count + word_length == end_char:
                end_word = i
                break
            char_count += word_length + 1  # Add 1 for the space

        # Append the word positions to the list
        entities.append((start_word, end_word, entity['type']))

    # Create a list of word positions for each entity
    sample = {
        "tokenized_text": words,
        "ner": entities
    }

    return sample


# create dataset
def create_dataset(path):
    train, dev, test, labels = open_content(path)
    train_dataset = []
    dev_dataset = []
    test_dataset = []
    for data in train:
        train_dataset.append(process(data))
    for data in dev:
        dev_dataset.append(process(data))
    for data in test:
        test_dataset.append(process(data))
    return train_dataset, dev_dataset, test_dataset, labels


@torch.no_grad()
def get_for_one_path(path, model):
    # load the dataset
    _, _, test_dataset, entity_types = create_dataset(path)

    data_name = path.split("/")[-1]  # get the name of the dataset

    # check if the dataset is flat_ner
    flat_ner = True
    if any([i in data_name for i in ["ACE", "GENIA", "Corpus"]]):
        flat_ner = False

    # evaluate the model
    results, f1 = model.evaluate(test_dataset, flat_ner=flat_ner, threshold=0.5, batch_size=12,
                                 entity_types=entity_types)
    return data_name, results, f1


def get_for_all_path(model, steps, log_dir, data_paths):
    all_paths = glob.glob(f"{data_paths}/*")

    all_paths = sorted(all_paths)

    # move the model to the device
    device = next(model.parameters()).device
    model.to(device)
    # set the model to eval mode
    model.eval()

    # log the results
    save_path = os.path.join(log_dir, "results.txt")

    with open(save_path, "a") as f:
        f.write("##############################################\n")
        # write step
        f.write("step: " + str(steps) + "\n")

    zero_shot_benc = ["mit-movie", "mit-restaurant", "CrossNER_AI", "CrossNER_literature", "CrossNER_music",
                      "CrossNER_politics", "CrossNER_science"]

    zero_shot_benc_results = {}
    all_results = {}  # without crossNER

    for p in tqdm(all_paths):
        if "sample_" not in p:
            data_name, results, f1 = get_for_one_path(p, model)
            # write to file
            with open(save_path, "a") as f:
                f.write(data_name + "\n")
                f.write(str(results) + "\n")

            if data_name in zero_shot_benc:
                zero_shot_benc_results[data_name] = f1
            else:
                all_results[data_name] = f1

    avg_all = sum(all_results.values()) / len(all_results)
    avg_zs = sum(zero_shot_benc_results.values()) / len(zero_shot_benc_results)

    save_path_table = os.path.join(log_dir, "tables.txt")

    # results for all datasets except crossNER
    table_bench_all = ""
    for k, v in all_results.items():
        table_bench_all += f"{k:20}: {v:.1%}\n"
    # (20 size aswell for average i.e. :20)
    table_bench_all += f"{'Average':20}: {avg_all:.1%}"

    # results for zero-shot benchmark
    table_bench_zeroshot = ""
    for k, v in zero_shot_benc_results.items():
        table_bench_zeroshot += f"{k:20}: {v:.1%}\n"
    table_bench_zeroshot += f"{'Average':20}: {avg_zs:.1%}"

    # write to file
    with open(save_path_table, "a") as f:
        f.write("##############################################\n")
        f.write("step: " + str(steps) + "\n")
        f.write("Table for all datasets except crossNER\n")
        f.write(table_bench_all + "\n\n")
        f.write("Table for zero-shot benchmark\n")
        f.write(table_bench_zeroshot + "\n")
        f.write("##############################################\n\n")


def sample_train_data(data_paths, sample_size=10000):
    all_paths = glob.glob(f"{data_paths}/*")

    all_paths = sorted(all_paths)

    # to exclude the zero-shot benchmark datasets
    zero_shot_benc = ["CrossNER_AI", "CrossNER_literature", "CrossNER_music",
                      "CrossNER_politics", "CrossNER_science", "ACE 2004"]

    new_train = []
    # take 10k samples from each dataset
    for p in tqdm(all_paths):
        if any([i in p for i in zero_shot_benc]):
            continue
        train, dev, test, labels = create_dataset(p)

        # add label key to the train data
        for i in range(len(train)):
            train[i]["label"] = labels

        random.shuffle(train)
        train = train[:sample_size]
        new_train.extend(train)

    return new_train

```

## File: glirel/modules/base.py

<a name='file-glirel-modules-base.py'></a>
*Description*: This is a Python script.

```python
from collections import defaultdict
from typing import List, Tuple, Dict

import torch
from torch import nn
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import DataLoader
import random
import os
import logging
from copy import copy, deepcopy


logger = logging.getLogger(__name__)

def insert_entity_markers(tokens, span_idx, relations, entity_start_token, entity_end_token):
    """
    tokens: List[str] - tokenized input sequence
    span_idx: List[Tuple[int, int]] - list of (start_idx, end_idx) for entities
    relations: List[Dict] - list of relation dictionaries
    entity_start_token: str - entity start token
    entity_end_token: str - entity end token

    ['<e>', 'John', 'Doe', '</e>', 'is', 'a', 'software', 'engineer', 'at', '<e>', 'Google', '</e>', 'in', '<e>', 'Dublin', '</e>', '.']
    """
    if entity_start_token in tokens or entity_end_token in tokens:
        # logger.warning(f"Entity markers already present in tokens. Skipping insertion.")
        return tokens, span_idx, relations
    prev_tokens = copy(tokens)
    prev_relations = deepcopy(relations)
    offset = 0
    adjusted_span_idx = []
    span2adjusted_span = {}
    for start, end in sorted(span_idx, key=lambda x: x[0]):
        adjusted_start = start + offset
        tokens.insert(start + offset, entity_start_token)
        offset += 1
        tokens.insert(end + offset + 1, entity_end_token)
        offset += 1
        adjusted_end = end + offset
        adjusted_span_idx.append((adjusted_start, adjusted_end))
        span2adjusted_span[(start, end)] = (adjusted_start, adjusted_end)

    adjusted_relations = []
    for rel in relations:
        head_idx = tuple(rel['head']['position'])
        tail_idx = tuple(rel['tail']['position'])
        try:
            adjusted_head_idx = span2adjusted_span[head_idx]
        except:
            import ipdb; ipdb.set_trace()
        try:
            adjusted_tail_idx = span2adjusted_span[tail_idx]
        except:
            import ipdb; ipdb.set_trace()
        rel['head']['position'] = list(adjusted_head_idx)
        rel['tail']['position'] = list(adjusted_tail_idx)
        adjusted_relations.append(rel)
    
    adjusted_relations = sorted(adjusted_relations, key=lambda x: x['head']['position'][0])
    return tokens, adjusted_span_idx, adjusted_relations

def generate_entity_pairs_indices(span_idx, max_distance: int | None = None, device: str = 'cpu'):
    """
    Generates a combined entity pair indices tensor for both coreference and relation classification.
    Coreference pairs are unidirectional (i < j), and relation pairs are bidirectional (i ≠ j),
    with a distance constraint for relation pairs if specified.

    Args:
        span_idx: Tensor of shape [num_entities, 2], representing the start and end indices of each entity.
        max_distance: Integer, the maximum allowed token distance for relation classification (None for coreference).
        
    Returns:
        combined_pairs: Tensor of shape [num_pairs, 2, 2], representing start/end indices for all valid entity pairs.
    """
    num_entities = span_idx.size(0)  # [num_ents, 2]

    # Expand and tile to create all possible pairs
    span_idx_expanded = span_idx.unsqueeze(1).expand(-1, num_entities, -1)  # ([num_entities, num_entities, 2])
    span_idx_tiled = span_idx.unsqueeze(0).expand(num_entities, -1, -1)     # ([num_entities, num_entities, 2])

    # Indices for self-pair exclusion and directionality
    indices = torch.arange(num_entities, device=device)
    indices_expanded = indices.unsqueeze(1).expand(-1, num_entities)
    indices_tiled = indices.unsqueeze(0).expand(num_entities, -1)

    # Coreference: unidirectional pairs (i < j)
    coref_mask = indices_expanded < indices_tiled  # Keep only pairs where i < j

    # Relation pairs: bidirectional pairs, excluding self-pairs (i != j)
    relation_mask = indices_expanded != indices_tiled

    # Compute token distances between entity pairs (based on start indices)
    start_idx_expanded = span_idx[:, 0].unsqueeze(1).expand(-1, num_entities)  # [num_entities, num_entities]
    start_idx_tiled = span_idx[:, 0].unsqueeze(0).expand(num_entities, -1)     # [num_entities, num_entities]
    token_distances = torch.abs(start_idx_expanded - start_idx_tiled)  # [num_entities, num_entities]

    # Apply distance constraint for relation pairs
    if max_distance is not None:
        distance_mask = token_distances <= max_distance
        relation_mask = relation_mask & distance_mask

    # Combine coreference and relation masks
    combined_mask = coref_mask | relation_mask  # Union of coref and relation masks

    # Apply the combined mask to filter pairs
    span_idx_filtered_expanded = span_idx_expanded[combined_mask]
    span_idx_filtered_tiled = span_idx_tiled[combined_mask]

    # Stack the pairs back into shape [num_pairs, 2, 2]
    combined_pairs = torch.stack((span_idx_filtered_expanded, span_idx_filtered_tiled), dim=1)

    return combined_pairs  # ([num_pairs, 2, 2])


class InstructBase(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.max_width = config.max_width
        self.base_config = config
        self.base_config.coreference_label = getattr(config, "coreference_label", "SELF")  # NOTE: this label is given a special index to denote coreference (i.e -2)
        self.max_entity_pair_distance = config.max_entity_pair_distance
        self.device = torch.device(getattr(config, "device", "cuda" if torch.cuda.is_available() else "cpu"))

        self.base_config.entity_start_token, self.base_config.entity_end_token = "[E]", "[/E]"
        if self.base_config.span_marker_mode == 'markerv2':
            logger.info(f"Using SpanMarkerV2. Adding entity markers: {self.base_config.entity_start_token}, {self.base_config.entity_end_token}")

    def get_dict(self, spans, classes_to_id):
        dict_tag = defaultdict(int)
        for span in spans:
            if span[2] in classes_to_id:
                dict_tag[(span[0], span[1])] = classes_to_id[span[2]]
        return dict_tag
    
    def get_rel_dict(self, relations, classes_to_id):
        dict_tag = defaultdict(int)
        for rel in relations:
            if rel['relation_text'] in classes_to_id:
                dict_tag[(tuple(rel['head']['position']), tuple(rel['tail']['position']))] = classes_to_id[rel['relation_text']]
        return dict_tag
    
    def get_rel_labels(self, relations_idx, rel_label_dict, classes_to_id):
        # get the class for each relation pair

        relations_idx = relations_idx.tolist()

        # assign label if in dataset else 0
        rel_labels = []
        for rel in relations_idx:
            head_idx, tail_idx = tuple(rel[0]), tuple(rel[1])
            if (head_idx, tail_idx) in rel_label_dict:
                label = rel_label_dict[(head_idx, tail_idx)]
                rel_labels.append(label)
            # elif (tail_idx, head_idx) in rel_label_dict:
            #     # assign the same label as the reverse relation (if it exists)
            #     label = rel_label_dict[(head_idx, tail_idx)]
            #     rel_labels.append(label)
            else:
                rel_labels.append(0)

        return rel_labels
    

    def preprocess_spans(self, tokens, ner, classes_to_id, relations):

        max_len = self.base_config.max_len

        if len(tokens) > max_len:
            logger.warning(f"Token length {len(tokens)} is longer than max length {max_len}. Truncating.")
            seq_length = max_len
            tokens = tokens[:max_len]
        else:
            seq_length = len(tokens)

        spans_idx = []


        for ner_span in ner:
            start, end = ner_span[0], ner_span[1]
            spans_idx.append((start, end))

        if hasattr(self.base_config, "add_entity_markers") and self.base_config.add_entity_markers:
            tokens, spans_idx, relations = insert_entity_markers(
                tokens, spans_idx, relations, 
                self.base_config.entity_start_token, self.base_config.entity_end_token
            )
            seq_length = len(tokens)

        # MAX_SPANS = 35     # NOTE: max number of span pairs -- can be increased with more VRAM
        # if len(spans_idx) > MAX_SPANS:
        #     logger.warn(f"Truncating relations and ner spans because there are too many ({len(spans_idx)} > {MAX_SPANS})")
        #     spans_idx = spans_idx[: MAX_SPANS]
        spans_idx_list = spans_idx
              
        spans_idx = torch.tensor(spans_idx, dtype=torch.long, device=self.device)  # [num_possible_spans, 2]
        relations_idx = generate_entity_pairs_indices(
            spans_idx, max_distance=self.base_config.max_entity_pair_distance,
            device=self.device
        )  # [num_ent_pairs, 2, 2]

        if relations is not None:  # training
            included_relations = []
            # if we need to truncate the number of relations
            for rel in relations:
                head_idx = (rel['head']['position'][0], rel['head']['position'][1]) 
                tail_idx = (rel['tail']['position'][0], rel['tail']['position'][1]) 
                if head_idx in spans_idx_list and tail_idx in spans_idx_list:
                    included_relations.append(rel)

            relations = included_relations

            # get the class for each relation pair
            rel_label_dict = self.get_rel_dict(relations, classes_to_id)
            # 0 for null labels
            rel_label = torch.tensor(
                self.get_rel_labels(relations_idx, rel_label_dict, classes_to_id),
                dtype=torch.long, device=self.device
            )  # [num_ent_pairs]

        else:  # no labels --> predict
            rel_label_dict = defaultdict(int)
            rel_label = torch.tensor([rel_label_dict[i] for i in relations_idx], dtype=torch.long, device=self.device)


        # mask for valid spans
        valid_span_mask = spans_idx[:, 1] > seq_length - 1

        # mask invalid positions
        span_label = torch.ones(spans_idx.size(0), dtype=torch.long, device=self.device)
        span_label = span_label.masked_fill(valid_span_mask, -1)  # [num_possible_spans]

        # mask for valid relations
        valid_rel_mask = relations_idx[:, 1, 1] > seq_length - 1
        rel_label = rel_label.masked_fill(valid_rel_mask, -1)


        out = {
            'tokens': tokens,
            'span_idx': spans_idx,
            'span_label': span_label,
            'seq_length': seq_length,
            'entities': ner,
            'relations': relations if 'relations' in locals() else None,
            'rel_label': rel_label if 'rel_label' in locals() else None,
            'relations_idx': relations_idx if 'relations_idx' in locals() else None,
        }
        return out

    def collate_fn(self, batch_list, relation_types=None, train_relation_types=None, device=None):
        if device:
            self.device = torch.device(device)
        assert hasattr(self.base_config, "fixed_relation_types"), "`fixed_relation_types` must be set in config"
        class_to_ids = []
        id_to_classes = []

        def _substitute_coref_label(coref_label, class_to_ids):
            """
            Assigns a special index to the coreference label. 
            This is used to distinguish coreference from other relation types if we decide to compute coreference loss separately.
            """
            if isinstance(coref_label, str):
                coref_label = [coref_label.lower()]
            else:
                coref_label = [l.lower() for l in coref_label]
            for key in class_to_ids.keys():
                if key.lower() in coref_label:
                    class_to_ids[key] = class_to_ids[key] * -50

            return class_to_ids

        # batch_list: list of dict containing tokens, ner
        if relation_types is None:
            # training
            self.processing_mode = "training"
            assert train_relation_types is not None, "`train_relation_types` must be provided for relation extraction data loader"
            negs = self.get_negatives_rel(train_relation_types, 100)
            for b in batch_list:
                # negs = b["negative"]
                random.shuffle(negs)


                positive_types = list(set([el['relation_text'] for el in b['relations']]))

                # make up to num_train_rel_types using as many negatives as needed (none if there's already enough positives)
                remainder_relations = max(0, int(self.base_config.num_train_rel_types) - len(positive_types))
                # remainder_relations -= 1  # save space for "no_relation"
                negs_i = [negative for negative in negs if negative not in positive_types][:remainder_relations]

                # this is the list of all possible relation types (positive and negative)
                types = list(set(positive_types + negs_i))

                # shuffle (every epoch)
                if getattr(self.base_config, "shuffle_types", True):
                    random.shuffle(types)

                # random drop
                if len(types) != 0 and self.base_config.random_drop:
                    num_rels = random.randint(1, len(types))
                    types = types[ :num_rels]

                types = types[ : self.base_config.num_train_rel_types]


                # supervised training
                if "label" in b:
                    types = sorted(b["label"])

                class_to_id = {k: v for v, k in enumerate(types, start=1)}
                class_to_id = _substitute_coref_label(self.base_config.coreference_label, class_to_id)
                id_to_class = {k: v for v, k in class_to_id.items()}
                class_to_ids.append(class_to_id)
                id_to_classes.append(id_to_class)

            batch = [
                self.preprocess_spans(b["tokenized_text"], b["ner"], class_to_ids[i], b.get('relations')) for i, b in enumerate(batch_list)
            ]

        else:
            # evaluation
            self.processing_mode = "evaluation"
            if (self.base_config.fixed_relation_types is True):
                # relation labels are fixed across all batches, e.g for evaluating m=15, etc
                class_to_id = {k: v for v, k in enumerate(relation_types, start=1)}
                # class_to_id = _substitute_coref_label(self.base_config.coreference_label, class_to_id)  # NOTE: change COREFERENCE LABEL TO -2
                id_to_class = {k: v for v, k in class_to_id.items()}
                class_to_ids = [class_to_id] * len(batch_list)
                id_to_classes = [id_to_class] * len(batch_list)
            else:
                # relation labels are different for each batch
                for i, b in enumerate(batch_list):
                    if 'relations' in b:
                        # eval during training
                        instance_relation_types = list(set([el['relation_text'] for el in b['relations']]))
                    else:
                        # provided batch of label lists in the wild
                        instance_relation_types = list(set([r for r in relation_types[i]]))
                    class_to_id = {k: v for v, k in enumerate(instance_relation_types, start=1)}
                    # class_to_id = _substitute_coref_label(self.base_config.coreference_label, class_to_id)  # NOTE: change COREFERENCE LABEL TO -2
                    id_to_class = {k: v for v, k in class_to_id.items()}
                    class_to_ids.append(class_to_id)
                    id_to_classes.append(id_to_class)
                # logger.info(f"Number of eval relation types per instance: {[len(d) for d in class_to_ids]}")

            
            batch = [
                self.preprocess_spans(b["tokenized_text"], b["ner"], class_to_ids[i], b.get('relations')) for i, b in enumerate(batch_list)
            ]

        span_idx = pad_sequence(
            [b['span_idx'] for b in batch], batch_first=True, padding_value=0
        )

        span_label = pad_sequence(
            [el['span_label'] for el in batch], batch_first=True, padding_value=-1
        )

        rel_label = pad_sequence(
            [el['rel_label'] for el in batch], batch_first=True, padding_value=-1
        )

        relations_idx = pad_sequence(
            [el['relations_idx'] for el in batch], batch_first=True, padding_value=-1
        )

        return {
            'seq_length': torch.tensor([el['seq_length'] for el in batch], dtype=torch.long, device=self.device),
            'span_idx': span_idx,
            'tokens': [el['tokens'] for el in batch],
            'span_mask': span_label != -1,
            'span_label': span_label,
            'rel_label': rel_label if 'rel_label' in locals() else None,
            'relations_idx': relations_idx,
            'entities': [el['entities'] for el in batch],
            'relations': [el.get('relations') for el in batch],
            'classes_to_id': class_to_ids,
            'id_to_classes': id_to_classes,
        }

    @staticmethod
    def get_negatives(batch_list, sampled_neg=5):
        ent_types = []
        for b in batch_list:
            types = set([el[2] for el in b['ner']])
            ent_types.extend(list(types))
        ent_types = list(set(ent_types))
        # sample negatives
        random.shuffle(ent_types)
        return ent_types[:sampled_neg]
    
    @staticmethod
    def get_negatives_rel(train_relation_types, sampled_neg=100):
        # sample negatives
        random.shuffle(train_relation_types)
        return train_relation_types[:sampled_neg]

    def create_dataloader(self, data, relation_types=None, train_relation_types=None, **kwargs):
        return DataLoader(data, collate_fn=lambda x: self.collate_fn(x, relation_types, train_relation_types), **kwargs)

    def set_sampling_params(self, max_types, shuffle_types, random_drop, max_neg_type_ratio, max_len, num_train_rel_types=None):
        """
        Sets sampling parameters on the given model.

        Parameters:
        - model: The model object to update.
        - max_types: Maximum types parameter.
        - shuffle_types: Boolean indicating whether to shuffle types.
        - random_drop: Boolean indicating whether to randomly drop elements.
        - max_neg_type_ratio: Maximum negative type ratio.
        - max_len: Maximum length parameter.
        """
        self.base_config.max_types = max_types
        self.base_config.shuffle_types = shuffle_types
        self.base_config.random_drop = random_drop
        self.base_config.max_neg_type_ratio = max_neg_type_ratio
        self.base_config.max_len = max_len
        self.base_config.num_train_rel_types = num_train_rel_types

```

## File: glirel/modules/___init__.py

<a name='file-glirel-modules-___init__.py'></a>
*Description*: This is a Python script.

```python

```

## File: glirel/modules/layers.py

<a name='file-glirel-modules-layers.py'></a>
*Description*: This is a Python script.

```python
import torch
import torch.nn.functional as F
from torch import nn
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence

from .utils import down_weight_loss


class LstmSeq2SeqEncoder(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers=1, dropout=0., bidirectional=False):
        super(LstmSeq2SeqEncoder, self).__init__()
        self.lstm = nn.LSTM(input_size=input_size,
                            hidden_size=hidden_size,
                            num_layers=num_layers,
                            dropout=dropout,
                            bidirectional=bidirectional,
                            batch_first=True)

    def forward(self, x, mask, hidden=None):
        # Packing the input sequence
        lengths = mask.sum(dim=1).cpu()
        packed_x = pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)

        # Passing packed sequence through LSTM
        packed_output, hidden = self.lstm(packed_x, hidden)

        # Unpacking the output sequence
        output, _ = pad_packed_sequence(packed_output, batch_first=True)

        return output


# https://github.com/urchade/EnriCo/blob/main/modules/layers.py

def MLP(units, dropout, activation=nn.ReLU):
    # convert to integer
    units = [int(u) for u in units]

    assert len(units) >= 2
    layers = []
    for i in range(len(units) - 2):
        layers.append(nn.Linear(units[i], units[i + 1]))
        layers.append(activation())
        layers.append(nn.Dropout(dropout))
    layers.append(nn.Linear(units[-2], units[-1]))
    return nn.Sequential(*layers)


class FilteringLayer(nn.Module):
    def __init__(self, hidden_size):
        super().__init__()

        self.filter_layer = nn.Linear(hidden_size, 2)

    def forward(self, embeds, label):

        # Extract dimensions
        B, num_spans, D = embeds.shape

        # Compute score using a predefined filtering function
        score = self.filter_layer(embeds)  # Shape: [B, num_spans, num_classes]

        # Modify label to binary (0 for negative class, 1 for positive)
        label_m = label.clone()
        label_m[label_m > 0] = 1

        # Initialize the loss
        filter_loss = 0
        if self.training:
            # Compute the loss if in training mode
            filter_loss = down_weight_loss(score.view(B * num_spans, -1),
                                           label_m.view(-1),
                                           sample_rate=0.,
                                           is_logit=True)

        # Compute the filter score (difference between positive and negative class scores)
        filter_score = score[..., 1] - score[..., 0]  # Shape: [B, num_spans]

        # Mask out filter scores for ignored labels
        filter_score = filter_score.masked_fill(label == -1, -1e9)

        if self.training:
            filter_score = filter_score.masked_fill(label_m > 0, 1e5)

        return filter_score, filter_loss


class CrossAtt(nn.Module):
    def __init__(self, d_model, num_heads):
        super(CrossAtt, self).__init__()

        assert d_model % num_heads == 0
        self.mha = nn.MultiheadAttention(d_model, num_heads, batch_first=True, add_zero_attn=True)

    def forward(self, query, kv, key_padding_mask=None):
        # query: [batch, seq_len, d_model]
        return self.mha(query, kv, kv, key_padding_mask=key_padding_mask)[0]


class ReadProcess(nn.Module):
    def __init__(self, d_model, num_heads, ffn_mul=4, dropout=0.1, read_only=False):
        super().__init__()

        self.read_only = read_only

        self.read = CrossAtt(d_model, num_heads)
        self.norm_read = nn.LayerNorm(d_model)

        if not read_only:
            self.process = CrossAtt(d_model, num_heads)
            self.norm_process = nn.LayerNorm(d_model)

        self.ffn = MLP([d_model, d_model * ffn_mul, d_model], dropout, activation=nn.GELU)
        self.norm_ffn = nn.LayerNorm(d_model)

    def forward(self, input_embed, word_rep, input_mask, word_mask):
        # input: [batch, seq_len, d_model]
        input_mask = input_mask == False
        word_mask = word_mask == False

        # Cross-attention
        x = input_embed + self.read(self.norm_read(input_embed), word_rep, key_padding_mask=word_mask)

        # Self-attention
        if not self.read_only:
            x = x + self.process(self.norm_process(x), x, key_padding_mask=input_mask)

        return x + self.norm_ffn(self.ffn(x))


class RefineLayer(nn.Module):
    def __init__(self, d_model, num_heads, num_layers=1, ffn_mul=4, dropout=0.1, read_only=False):
        super().__init__()

        self.blocks = nn.ModuleList([ReadProcess(d_model, num_heads, ffn_mul, dropout, read_only)
                                     for _ in range(num_layers)])

        self.output = nn.Linear(d_model, d_model)

    def forward(self, input_embed, word_rep, input_mask, word_mask):
        for block in self.blocks:
            input_embed = block(input_embed, word_rep, input_mask, word_mask)
        return self.output(input_embed)


class ScorerLayer(nn.Module):
    def __init__(self, scoring_type="dot", hidden_size=768, dropout=0.1):
        super().__init__()

        self.scoring_type = scoring_type

        if scoring_type == "concat_proj":
            self.proj = MLP([hidden_size * 4, hidden_size * 4, 1], dropout)
        elif scoring_type == "dot_thresh":
            self.proj_thresh = MLP([hidden_size, hidden_size * 4, 2], dropout)
            self.proj_type = MLP([hidden_size, hidden_size * 4, hidden_size], dropout)
        elif scoring_type == "dot_norm":
            self.dy_bias_type = MLP([hidden_size, hidden_size * 4, 1], dropout)
            self.dy_bias_rel = MLP([hidden_size, hidden_size * 4, 1], dropout)
            self.bias = nn.Parameter(torch.tensor(-10.0))

    def forward(self, candidate_pair_rep, rel_type_rep):
        # candidate_pair_rep: [B, N, D]
        # rel_type_rep: [B, T, D]
        if self.scoring_type == "dot":
            return torch.einsum('BKD,BCD->BKC', candidate_pair_rep, rel_type_rep) # ([B, num_pairs, num_classes])

        elif self.scoring_type == "dot_thresh":
            # compute the scaling factor and threshold
            B, T, D = rel_type_rep.size()
            scaler = self.proj_thresh(rel_type_rep)  # [B, T, 2]
            # alpha: scaling factor, beta: threshold
            alpha, beta = scaler[..., 0].view(B, 1, T), scaler[..., 1].view(B, 1, T)
            alpha = F.softplus(alpha)  # reason: alpha should be positive
            # project the relation type representation
            rel_type_rep = self.proj_type(rel_type_rep)  # [B, T, D]
            # compute the score (before sigmoid)
            score = torch.einsum("bnd,btd->bnt", candidate_pair_rep, rel_type_rep)  # [B, N, T]
            return (score + beta) * alpha  # [B, N, T]

        elif self.scoring_type == "dot_norm":
            score = torch.einsum("bnd,btd->bnt", candidate_pair_rep, rel_type_rep)  # [B, N, T]
            bias_1 = self.dy_bias_type(rel_type_rep).transpose(1, 2)  # [B, 1, T]
            bias_2 = self.dy_bias_rel(candidate_pair_rep)  # [B, N, 1]
            return score + self.bias + bias_1 + bias_2

        elif self.scoring_type == "concat_proj":
            prod_features = candidate_pair_rep.unsqueeze(2) * rel_type_rep.unsqueeze(1)  # [B, N, T, D]
            diff_features = candidate_pair_rep.unsqueeze(2) - rel_type_rep.unsqueeze(1)  # [B, N, T, D]
            expanded_pair_rep = candidate_pair_rep.unsqueeze(2).repeat(1, 1, rel_type_rep.size(1), 1)
            expanded_rel_type_rep = rel_type_rep.unsqueeze(1).repeat(1, candidate_pair_rep.size(1), 1, 1)
            features = torch.cat([prod_features, diff_features, expanded_pair_rep, expanded_rel_type_rep],
                                 dim=-1)  # [B, N, T, 2D]
            return self.proj(features).squeeze(-1)
```

## File: glirel/modules/rel_rep.py

<a name='file-glirel-modules-rel_rep.py'></a>
*Description*: This is a Python script.

```python
import torch
from torch import nn
from glirel.modules.span_rep import create_projection_layer, SpanMarkerV0, extract_elements
import torch.nn.functional as F
import logging

logger = logging.getLogger(__name__)




class SpanMarkerV1(nn.Module):
    """
    Marks and projects span endpoints using an MLP.
    """

    def __init__(self, hidden_size: int, max_width: int, dropout: float = 0.4):
        super().__init__()
        self.max_width = max_width
        self.project_start = create_projection_layer(hidden_size, dropout)
        self.project_end = create_projection_layer(hidden_size, dropout)

        self.out_project = create_projection_layer(hidden_size * 2, dropout, hidden_size)

    def forward(self, h: torch.Tensor, span_idx: torch.Tensor) -> torch.Tensor:
        B, L, D = h.size()
        # span_idx.shape    ([B, num_possible_spans, 2])

        start_rep = self.project_start(h)  # ([B, L, D])
        end_rep = self.project_end(h)      # ([B, L, D])

        start_span_rep = extract_elements(start_rep, span_idx[:, :, 0])  # ([B, num_possible_spans, D])
        end_span_rep = extract_elements(end_rep, span_idx[:, :, 1])      # ([B, num_possible_spans, D])

        cat = torch.cat([start_span_rep, end_span_rep], dim=-1).relu()   # ([B, num_possible_spans, D*2])

        return self.out_project(cat) # ([B, number_of_entities, D])               #### .view(B, L, self.max_width, D)
    
class SpanMarkerV2(nn.Module):
    """
    Efficiently computes span representations by pooling over embeddings.
    """

    def __init__(self, hidden_size: int, max_width: int, dropout: float = 0.4):
        super().__init__()
        self.max_width = max_width
        self.projection = create_projection_layer(hidden_size, dropout)

    def forward(self, h: torch.Tensor, span_idx: torch.Tensor) -> torch.Tensor:
        """
        h: [B, L, D] - Hidden states from the encoder.
        span_idx: [B, num_spans, 2] - Start and end indices of spans.
        Returns:
            span_reps: [B, num_spans, D] - Pooled span representations.
        """
        B, L, D = h.size()
        _, num_spans, _ = span_idx.size()

        # Compute lengths of each span
        lengths = span_idx[:, :, 1] - span_idx[:, :, 0] + 1  # [B, num_spans]
        max_span_length = lengths.max().item()

        # Create position offsets
        position_offsets = torch.arange(max_span_length, device=h.device).unsqueeze(0).unsqueeze(0)  # [1, 1, max_span_length]

        # Compute positions
        start_positions = span_idx[:, :, 0].unsqueeze(-1)  # [B, num_spans, 1]
        positions = start_positions + position_offsets  # [B, num_spans, max_span_length]

        # Create mask for valid positions
        span_mask = (position_offsets < lengths.unsqueeze(-1))  # [B, num_spans, max_span_length]

        # Clamp positions to valid range
        positions = positions * span_mask.long()
        positions = positions.clamp(0, L - 1)  # Ensure indices are within [0, L - 1]

        # Flatten positions for gathering
        positions_flat = positions.view(B, -1)  # [B, num_spans * max_span_length]

        # Gather embeddings
        h_expanded = h.unsqueeze(1).expand(-1, num_spans, -1, -1)  # [B, num_spans, L, D]
        h_expanded = h_expanded.contiguous().view(B * num_spans, L, D)
        positions_flat = positions_flat.view(B * num_spans, -1)
        gathered_embeddings = h_expanded.gather(1, positions_flat.unsqueeze(-1).expand(-1, -1, D))  # [B * num_spans, max_span_length, D]

        # Reshape to [B, num_spans, max_span_length, D]
        gathered_embeddings = gathered_embeddings.view(B, num_spans, max_span_length, D)

        # Apply mask
        span_mask = span_mask.float().unsqueeze(-1)  # [B, num_spans, max_span_length, 1]
        sum_embeddings = (gathered_embeddings * span_mask).sum(dim=2)  # [B, num_spans, D]
        span_lengths = lengths.float().unsqueeze(-1)  # [B, num_spans, 1]

        # Compute mean embeddings
        span_reps = sum_embeddings / span_lengths  # [B, num_spans, D]

        # Apply projection layer
        span_reps = self.projection(span_reps)  # [B, num_spans, D]

        return span_reps


def get_entity_pair_reps(entity_reps):
        B, num_entities, D = entity_reps.shape

        # Create a tensor [B, num_entities, num_entities, D] by repeating entity_reps for pairing
        # Expanding entity_reps to pair each with every other
        entity_reps_expanded = entity_reps.unsqueeze(2).expand(-1, -1, num_entities, -1)
        entity_reps_tiled = entity_reps.unsqueeze(1).expand(-1, num_entities, -1, -1)

        
        # Concatenate the representations of all possible pairs
        # The shape becomes [B, num_entities, num_entities, 2D]
        # NOTE: OOM error can occur here -- if there's too many entities
        pair_reps = torch.cat([entity_reps_expanded, entity_reps_tiled], dim=3)  # [B, num_entities, num_entities, 2 * D]

        # Now we have an entity pair matrix where each [i, j] element is the pair combination
        # of the i-th and j-th entities. We need to mask the diagonal (self-pairs).

        # Create a mask to exclude self-pairs
        indices = torch.arange(num_entities)
        mask = (indices.unsqueeze(0) != indices.unsqueeze(1))  # Create a mask to exclude self-pairs
        mask = mask.unsqueeze(0).expand(B, -1, -1)           # Expand mask for all batches

        combined_pairs = pair_reps[mask].view(B, -1, 2*D)    # Reshape to [B, num_valid_pairs, 2*D]

        
        return combined_pairs


def get_entity_pair_reps_v2(entity_reps, span_idx, relations_idx):
    """
    Generates entity pair representations based on the given relation indices.
    
    Args:
        entity_reps: Tensor of shape [B, num_entities, D], representing the entity representations.
        span_idx: Tensor of shape [B, num_entities, 2], representing the start and end indices of each entity.
        relations_idx: Tensor of shape [B, num_relations, 2, 2], where the last two indices 
                      are the start and end indices of an entity pair (e.g. [[0, 4], [6, 8]]).
        
    Returns:
        relation_pairs: Tensor of shape [B, num_relations, 2 * D], representing the relation 
                        entity pair representations.
    """
    B, num_entities, D = entity_reps.shape
    _, num_relations, _, _ = relations_idx.shape

    # Extract start and end token indices for head and tail from relations_idx
    head_start_tokens = relations_idx[:, :, 0, 0]  # [B, num_relations]
    head_end_tokens = relations_idx[:, :, 0, 1]  # [B, num_relations]
    tail_start_tokens = relations_idx[:, :, 1, 0]  # [B, num_relations]
    tail_end_tokens = relations_idx[:, :, 1, 1]  # [B, num_relations]

    # Extract start and end token indices for each entity in span_idx
    entity_starts = span_idx[:, :, 0]  # [B, num_entities]
    entity_ends = span_idx[:, :, 1]    # [B, num_entities]

    # Create masks to identify which entity each token belongs to
    head_mask = (head_start_tokens.unsqueeze(2) == entity_starts.unsqueeze(1)) & (head_end_tokens.unsqueeze(2) == entity_ends.unsqueeze(1))  # [B, num_relations, num_entities]
    tail_mask = (tail_start_tokens.unsqueeze(2) == entity_starts.unsqueeze(1)) & (tail_end_tokens.unsqueeze(2) == entity_ends.unsqueeze(1))  # [B, num_relations, num_entities]

    # Use argmax to get the indices of the entities that match the tokens in head and tail
    head_entity_indices = torch.argmax(head_mask.int(), dim=2)  # [B, num_relations]
    tail_entity_indices = torch.argmax(tail_mask.int(), dim=2)  # [B, num_relations]

    # Gather the entity representations using the found indices
    head_entity_reps = torch.gather(entity_reps, 1, head_entity_indices.unsqueeze(-1).expand(-1, -1, D))  # [B, num_relations, D]
    tail_entity_reps = torch.gather(entity_reps, 1, tail_entity_indices.unsqueeze(-1).expand(-1, -1, D))  # [B, num_relations, D]

    # Concatenate head and tail representations for each relation
    relation_pairs = torch.cat([head_entity_reps, tail_entity_reps], dim=-1)  # [B, num_relations, 2 * D]

    return relation_pairs


class RelMarkerv0(nn.Module):
    """
    Marks and projects representations for all pairs of entities.
    """
    def __init__(self, span_mode: str, hidden_size: int, max_width: int, dropout: float = 0.4):
        super().__init__()
        if span_mode == 'markerv1':
            self.span_marker = SpanMarkerV1(hidden_size, max_width, dropout)
        elif span_mode == 'markerv2':
            self.span_marker = SpanMarkerV2(hidden_size, max_width, dropout)

        self.out_project = create_projection_layer(hidden_size * 2, dropout, hidden_size)

    def forward(self, h: torch.Tensor, span_idx: torch.Tensor, relations_idx: torch.Tensor = None) -> torch.Tensor:
        """
        h: torch.Tensor - The hidden states of the shape [batch_size, seq_len, hidden_size]
        span_idx: torch.Tensor - The span indices of entities of the shape [batch_size, num_entities, 2]
        """
        B, L, D = h.size()
        # [B, num_entities, 2]  -->  span_idx.size()
        entity_reps = self.span_marker(h, span_idx)  #  ([B, number_of_entities, D])  

        combined_pairs = get_entity_pair_reps_v2(entity_reps, span_idx=span_idx, relations_idx=relations_idx)
        # combined_pairs = get_entity_pair_reps(entity_reps)

        # combined_pairs is now a tensor of shape [batch_size, num_pairs, 2*hidden_size]
        # where num_pairs is num_entities * (num_entities - 1) / 2, the number of unique pairs.

        combined_pairs_out = self.out_project(combined_pairs)


        return combined_pairs_out


class RelRepLayer(nn.Module):
    """
    Various span representation approaches
    """

    def __init__(self, hidden_size, max_width, rel_mode, span_mode, **kwargs):
        super().__init__()

        if rel_mode == 'marker':
            self.rel_rep_layer = RelMarkerv0(span_mode, hidden_size, max_width, **kwargs)
        else:
            raise ValueError(f'Unknown rel mode {rel_mode}')

    def forward(self, x, *args, **kwargs):

        return self.rel_rep_layer(x, *args, **kwargs)

```

## File: glirel/modules/data_proc.py

<a name='file-glirel-modules-data_proc.py'></a>
*Description*: This is a Python script.

```python
import json
from tqdm import tqdm
# ast.literal_eval
import ast, re

path = 'train.json'

with open(path, 'r') as f:
    data = json.load(f)

def tokenize_text(text):
    return re.findall(r'\w+(?:[-_]\w+)*|\S', text)

def extract_entity_spans(entry):
    text = ""
    len_start = len("What describes ")
    len_end = len(" in the text?")
    entity_types = []
    entity_texts = []

    for c in entry['conversations']:
        if c['from'] == 'human' and c['value'].startswith('Text: '):
            text = c['value'][len('Text: '):]
            tokenized_text = tokenize_text(text)

        if c['from'] == 'human' and c['value'].startswith('What describes '):

            c_type = c['value'][len_start:-len_end]
            c_type = c_type.replace(' ', '_')
            entity_types.append(c_type)

        elif c['from'] == 'gpt' and c['value'].startswith('['):
            if c['value'] == '[]':
                entity_types = entity_types[:-1]
                continue

            texts_ents = ast.literal_eval(c['value'])
            # replace space to _ in texts_ents
            entity_texts.extend(texts_ents)
            num_repeat = len(texts_ents) - 1
            entity_types.extend([entity_types[-1]] * num_repeat)

    entity_spans = []
    for j, entity_text in enumerate(entity_texts):
        entity_tokens = tokenize_text(entity_text)
        matches = []
        for i in range(len(tokenized_text) - len(entity_tokens) + 1):
            if " ".join(tokenized_text[i:i + len(entity_tokens)]).lower() == " ".join(entity_tokens).lower():
                matches.append((i, i + len(entity_tokens) - 1, entity_types[j]))
        if matches:
            entity_spans.extend(matches)

    return entity_spans, tokenized_text

# Usage:
# Replace 'entry' with the specific entry from your JSON data
entry = data[17818]  # For example, taking the first entry
entity_spans, tokenized_text = extract_entity_spans(entry)
print("Entity Spans:", entity_spans)
#print("Tokenized Text:", tokenized_text)

# create a dict: {"tokenized_text": tokenized_text, "entity_spans": entity_spans}

all_data = []

for entry in tqdm(data):
    entity_spans, tokenized_text = extract_entity_spans(entry)
    all_data.append({"tokenized_text": tokenized_text, "ner": entity_spans})


with open('train_instruct.json', 'w') as f:
    json.dump(all_data, f)


```

## File: glirel/modules/test_rel_rep.py

<a name='file-glirel-modules-test_rel_rep.py'></a>
*Description*: This is a Python script.

```python
import torch
from rel_rep import get_entity_pair_reps
from base import generate_entity_pairs_indices


def test_forward_output_matches_data_processing():
    ''' 
    NOTE:   the input for get_entity_pair_reps() is 
            entity representation of shape ([B, number_of_entities, D])

            the input for generate_entity_pairs_indices() is
            a single instance of shape [number_of_entities, 2]

            for this test, we will be using input of shape ([B, number_of_entities, 2]) 
            This let's us visually inspect that the two methods are generating pairs of 
            entities/spans in the same order

    '''
    
    # Mock input data
    # must be same num_entities per example for rel_rep (because it expects padded input)
    span_idx = torch.tensor(
        [
            [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 
            [[21, 21], [22, 22], [23, 23], [24, 24], [25, 25]], 
            [[800, 800], [801, 801], [0, 0], [0, 0], [0, 0]],
            [[900, 900], [901, 901], [902, 902], [903, 903], [904, 904]],
        ]
    )      
    #  -->  ([B, number_of_entities, 2])  ([4, 5, 2])

    # we expect there to be head-tail entity pairs in both directions, but no self-pairs
    expected_output = torch.tensor([[[  1,   1,   2,   2],
         [  1,   1,   3,   3],
         [  1,   1,   4,   4],
         [  1,   1,   5,   5],
         [  2,   2,   1,   1],
         [  2,   2,   3,   3],
         [  2,   2,   4,   4],
         [  2,   2,   5,   5],
         [  3,   3,   1,   1],
         [  3,   3,   2,   2],
         [  3,   3,   4,   4],
         [  3,   3,   5,   5],
         [  4,   4,   1,   1],
         [  4,   4,   2,   2],
         [  4,   4,   3,   3],
         [  4,   4,   5,   5],
         [  5,   5,   1,   1],
         [  5,   5,   2,   2],
         [  5,   5,   3,   3],
         [  5,   5,   4,   4]],

        [[ 21,  21,  22,  22],
         [ 21,  21,  23,  23],
         [ 21,  21,  24,  24],
         [ 21,  21,  25,  25],
         [ 22,  22,  21,  21],
         [ 22,  22,  23,  23],
         [ 22,  22,  24,  24],
         [ 22,  22,  25,  25],
         [ 23,  23,  21,  21],
         [ 23,  23,  22,  22],
         [ 23,  23,  24,  24],
         [ 23,  23,  25,  25],
         [ 24,  24,  21,  21],
         [ 24,  24,  22,  22],
         [ 24,  24,  23,  23],
         [ 24,  24,  25,  25],
         [ 25,  25,  21,  21],
         [ 25,  25,  22,  22],
         [ 25,  25,  23,  23],
         [ 25,  25,  24,  24]],

        [[800, 800, 801, 801],
         [800, 800,   0,   0],
         [800, 800,   0,   0],
         [800, 800,   0,   0],
         [801, 801, 800, 800],
         [801, 801,   0,   0],
         [801, 801,   0,   0],
         [801, 801,   0,   0],
         [  0,   0, 800, 800],
         [  0,   0, 801, 801],
         [  0,   0,   0,   0],
         [  0,   0,   0,   0],
         [  0,   0, 800, 800],
         [  0,   0, 801, 801],
         [  0,   0,   0,   0],
         [  0,   0,   0,   0],
         [  0,   0, 800, 800],
         [  0,   0, 801, 801],
         [  0,   0,   0,   0],
         [  0,   0,   0,   0]],

        [[900, 900, 901, 901],
         [900, 900, 902, 902],
         [900, 900, 903, 903],
         [900, 900, 904, 904],
         [901, 901, 900, 900],
         [901, 901, 902, 902],
         [901, 901, 903, 903],
         [901, 901, 904, 904],
         [902, 902, 900, 900],
         [902, 902, 901, 901],
         [902, 902, 903, 903],
         [902, 902, 904, 904],
         [903, 903, 900, 900],
         [903, 903, 901, 901],
         [903, 903, 902, 902],
         [903, 903, 904, 904],
         [904, 904, 900, 900],
         [904, 904, 901, 901],
         [904, 904, 902, 902],
         [904, 904, 903, 903]]])

    batch_size = span_idx.size(0)

    
    # Run the model's forward method for generating pairs
    rel_rep = get_entity_pair_reps(span_idx) #  -->  ([B, num_unique_pairs, 4])


    # Compute pairs of entities as done during precprocessing
    base_pairs_list = []
    batch_pairs_list = []
    for batch_i in range(batch_size):
        batch_pairs = generate_entity_pairs_indices(span_idx[batch_i])
        # batch_pairs  -->  ([num_unique_pairs, 2 ->start_index, 2 ->end_index])
        batch_pairs_list.append(batch_pairs)

        num_unique_pairs = batch_pairs.size(0)
        reshaped_batch_pairs = batch_pairs.reshape(num_unique_pairs, -1)
        # reshaped_batch_pairs  -->  ([num_unique_pairs, 4])

        base_pairs_list.append(reshaped_batch_pairs.tolist())

    base_pairs = torch.tensor(base_pairs_list)  # -->  ([B, num_unique_pairs, 4])

    
    # Assert the outputs are equal
    assert rel_rep.equal(base_pairs), "get_entity_pair_reps and generate_entity_pairs_indices do not give the same output"
    assert rel_rep.equal(expected_output), "get_entity_pair_reps does not match expected_output"


if __name__ == "__main__":
    test_forward_output_matches_data_processing()

```

## File: examples/finetune.py

<a name='file-examples-finetune.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import random
from glirel.model import GLiREL

import torch
import os

from glirel.model import load_config_as_namespace
from datetime import datetime
import logging

import sys
sys.path.append('..')
from train import train, dirty_split_data_by_relation_type


# ## 🏎️ Load Model

# In[3]:


model = GLiREL.from_pretrained("jackboyla/glirel_beta")


# ## ⚙️ Config

# In[4]:


config_file_path = '../configs/config_finetuning.yaml'
log_dir = '../logs/finetuning'


# In[5]:


logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])


# load config
config = load_config_as_namespace(config_file_path)

config.log_dir = log_dir
config.train_data = train_path

# set up logging
if config.log_dir is None:
    current_time = datetime.now().strftime("%Y-%m-%d__%H-%M-%S")
    config.log_dir = f'logs/{config.dataset_name}/{config.dataset_name}-{current_time}'
if not os.path.exists(config.log_dir):
    os.makedirs(config.log_dir)

log_file = "train.log"
log_file_path = os.path.join(config.log_dir, log_file)
if os.path.exists(log_file_path):
    os.remove(log_file_path)
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


# ## 📓 Prep Data

# In[6]:


train_path = "../data/sample.jsonl" # cannot be None
test_path = None  # can be None

assert os.path.exists(train_path), f"Train file not found: {train_path}"

with open(train_path, "r") as f:
    data = [json.loads(line) for line in f]

random.shuffle(data)

TEST_SET_RATIO = 0.1
TRAIN_SET_RATIO = 1 - TEST_SET_RATIO


if test_path is None:
    # if no test set provided, split the training data
    max_test_size = round(len(data)*TEST_SET_RATIO) + 1
    print(f"Splitting training data into training and test sets with max test size: {max_test_size}")
    train_dataset, test_dataset = dirty_split_data_by_relation_type(
        data, 
        num_unseen_rel_types=config.num_unseen_rel_types, 
        max_test_size=max_test_size,
        )
else:
    train_dataset = data
    with open(test_path, "r") as f:
        test_dataset = [json.loads(line) for line in f]

print('Train dataset size:', len(train_dataset))
print('Test dataset size:', len(test_dataset))


# ## 🚀 Train!

# In[7]:


# Get number of parameters (trainable and total)
num_params = sum(p.numel() for p in model.parameters())
num_trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
logger.info(f"Number of trainable parameters: {num_trainable_params} / {num_params}")

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = model.to(DEVICE)

lr_encoder = float(config.lr_encoder)
lr_others = float(config.lr_others)

optimizer = torch.optim.AdamW([
    # encoder
    {'params': model.token_rep_layer.parameters(), 'lr': lr_encoder},
    {'params': model.rnn.parameters(), 'lr': lr_others},
    # projection layers
    {'params': model.span_rep_layer.parameters(), 'lr': lr_others},
    {'params': model.prompt_rep_layer.parameters(), 'lr': lr_others},
])


logger.info("🚀 Relation extraction training started")
train(model, 
      optimizer, 
      train_dataset, 
      config, 
      eval_data=test_dataset, 
      num_steps=config.num_steps, 
      eval_every=config.eval_every, 
      log_dir=config.log_dir,
      wandb_log=False, 
      wandb_sweep=False, 
      warmup_ratio=config.warmup_ratio, 
      train_batch_size=config.train_batch_size, 
      device=DEVICE,
      use_amp=True if DEVICE == 'cuda' else False,
)


# ## 🥳 Load your finetuned model

# In[10]:


model = GLiREL.from_pretrained(f"{config.log_dir}/model_{config.eval_every}")

import spacy

nlp = spacy.load('en_core_web_sm')

text = 'Derren Nesbitt had a history of being cast in "Doctor Who", having played villainous warlord Tegana in the 1964 First Doctor serial "Marco Polo".'
doc = nlp(text)
tokens = [token.text for token in doc]

labels = ['country of origin', 'licensed to broadcast to', 'father', 'followed by', 'characters']

ner = [[26, 27, 'PERSON', 'Marco Polo'], [22, 23, 'Q2989412', 'First Doctor']] 

relations = model.predict_relations(tokens, labels, threshold=0.0, ner=ner, top_k=1)

print('Number of relations:', len(relations))

sorted_data_desc = sorted(relations, key=lambda x: x['score'], reverse=True)
print("\nDescending Order by Score:")
for item in sorted_data_desc:
    print(f"{item['head_text']} --> {item['label']} --> {item['tail_text']} | score: {item['score']}")


# In[ ]:





```

## File: configs/config_nyt.yaml

<a name='file-configs-config_nyt.yaml'></a>
*Description*: No specific description available.

```plaintext
# Learning Rate
lr_encoder: 1e-5
lr_others: 1e-4

# Training Parameters
num_steps: 20000
warmup_ratio: 0.1
train_batch_size: 8
eval_every: 500
gradient_accumulation: null
eval_batch_size: 32
num_layers_freeze: null
early_stopping_patience: 10
early_stopping_delta: 0.0


# Model Configuration
max_width: 12
model_name: microsoft/deberta-v3-large # hugging face model
fine_tune: true
subtoken_pooling: first
hidden_size: 1024
scorer: "dot"
span_mode: marker
refine_prompt: false
refine_relation: false
ffn_mul: 4
dropout: 0.4
scheduler: "cosine_with_warmup"  # "cosine_with_hard_restarts"
loss_func: "focal_loss" # "binary_cross_entropy_loss"  # "focal_loss"
alpha: 0.3
gamma: 3

# Coreference Resolution
coref_classifier: false
coref_loss_weight: 10.0

# Directory Paths
dataset_name: "nyt"
root_dir: ablation_backbone
train_data: "data/nyt/nyt_all.jsonl"

# "none" if no pretrained model 
prev_path: "none"


# Training Specifics
size_sup: -1
num_train_rel_types: 30   # number of relation labels to use in each given mini-batch
num_unseen_rel_types: 15
top_k: 1                  # number of relations predictions to return at evaluation time
random_drop: true       # randomly drop relation types
max_len: 384
eval_threshold: 0.2
max_entity_pair_distance: null
fixed_relation_types: true  # for eval: only use the given list of relation types (FewRel) for all batches
# fixed_relation_types: false   # for eval: use all relation types of a given batch (DocRED)


name: "large"



```

## File: configs/config_finetuning.yaml

<a name='file-configs-config_finetuning.yaml'></a>
*Description*: No specific description available.

```plaintext
# Learning Rate
lr_encoder: 1e-5
lr_others: 1e-4

# Training Parameters
num_steps: 21
warmup_ratio: 0.1
train_batch_size: 8
eval_every: 20
gradient_accumulation: null
eval_batch_size: 32

# Model Configuration
max_width: 12
model_name: microsoft/deberta-v3-small # hugging face model
fine_tune: true
subtoken_pooling: first
hidden_size: 768
scorer: "dot"
span_mode: marker
refine_prompt: false
refine_relation: false
ffn_mul: 4
dropout: 0.4
scheduler: "cosine_with_warmup"  # "cosine_with_hard_restarts"
loss_func: "binary_cross_entropy_loss"  # "binary_cross_entropy_loss"  # "focal_loss"
# alpha: 0.25
# gamma: 2

# Training Specifics
size_sup: -1
num_train_rel_types: 25   # number of relation labels to use in each given mini-batch
num_unseen_rel_types: 15
top_k: 1                  # number of relations predictions to return at evaluation time
random_drop: true       # randomly drop relation types
max_len: 384
eval_threshold: 0.1

name: "small"



```

## File: configs/config_redocred.yaml

<a name='file-configs-config_redocred.yaml'></a>
*Description*: No specific description available.

```plaintext
# Learning Rate
lr_encoder: 1e-5
lr_others: 1e-4
weight_decay_encoder: 0.01
weight_decay_other: 0.01

# Training Parameters
num_steps: 40000
warmup_ratio: 0.1
train_batch_size: 2
eval_every: 500
gradient_accumulation: 2  # null
eval_batch_size: 16
num_layers_freeze: null
early_stopping_patience: 12
early_stopping_delta: 0.0
threshold_search_metric: "macro_f1"
max_saves: 1

# Model Configuration
max_width: 12
model_name: microsoft/deberta-v3-large # hugging face model
fine_tune: true
subtoken_pooling: first
hidden_size: 768
scorer: "dot"
rel_mode: marker
span_marker_mode: markerv1
refine_prompt: false
refine_relation: false
ffn_mul: 4
dropout: 0.4
scheduler: "cosine_with_warmup"  # "cosine_with_hard_restarts"
loss_func: "binary_cross_entropy_loss" # "binary_cross_entropy_loss"  # "focal_loss"
alpha: 0.25
gamma: 2
# add_entity_markers: true
label_embed_strategy: "both"  # "label" "ent_token" "both"

# Coreference Resolution
coref_classifier: false
coref_loss_weight: 10.0
coreference_label: "SELF"

# Directory Paths
dataset_name: "redocred"
root_dir: ablation_backbone
train_data: "data/redocred_train.jsonl"
eval_data: "data/redocred_dev.jsonl"

# "none" if no pretrained model 
prev_path: "logs/zero_rel/zero_rel-2024-10-06__21-28-09/saved_at/model_70000"


# Training Specifics
size_sup: -1
num_train_rel_types: 15   # number of relation labels to use in each given mini-batch
top_k: 1                  # number of relations predictions to return at evaluation time
random_drop: true        # randomly drop relation types
max_len: 512
eval_threshold: [0.001, 0.01, 0.1, 0.2, 0.3, 0.5]
max_entity_pair_distance: 20
# fixed_relation_types: true  # for eval: only use the given list of relation types (FewRel) for all batches
fixed_relation_types: false   # for eval: use all relation types of a given batch (DocRED)
num_unseen_rel_types: 15      # for eval: will be ignored if `fixed_relation_types` is false

name: "large"



```

## File: configs/config_zero_rel.yaml

<a name='file-configs-config_zero_rel.yaml'></a>
*Description*: No specific description available.

```plaintext
# Learning Rate
lr_encoder: 1e-5
lr_others: 1e-4
weight_decay_encoder: 0.01
weight_decay_other: 0.01

# Training Parameters
num_steps: 100000
warmup_ratio: 0.1
train_batch_size: 1
eval_every: 3000
gradient_accumulation: 8 #null
eval_batch_size: 32
num_layers_freeze: null
early_stopping_patience: null
early_stopping_delta: 0.0
save_at: [200, 6000, 12000, 20000, 70000]
max_saves: 6

# Model Configuration
max_width: 12
model_name: microsoft/deberta-v3-large
fine_tune: true
subtoken_pooling: first
hidden_size: 768
scorer: "dot" # "dot_norm" # "dot"
rel_mode: marker
span_marker_mode: markerv1
refine_prompt: false
refine_relation: false
ffn_mul: 4
dropout: 0.4
scheduler: "cosine_with_warmup"  # "cosine_with_hard_restarts"
loss_func: "binary_cross_entropy_loss" # "binary_cross_entropy_loss"  # "focal_loss"
alpha: 0.6
gamma: 3
# add_entity_markers: true
label_embed_strategy: "both"  # "label" "ent_token" "both"


# Coreference Resolution
coref_classifier: false
coref_loss_weight: 10.0

# Directory Paths
dataset_name: "zero_rel"
root_dir: ablation_backbone
train_data: "data/zero_rel_all.jsonl"

# "none" if no pretrained model 
prev_path: "none"


# Training Specifics
size_sup: -1
num_train_rel_types: 25   # number of relation labels to use in each given mini-batch
num_unseen_rel_types: 15   # 15
top_k: 1                  # number of relations predictions to return at evaluation time
random_drop: true       # randomly drop relation types
max_len: 512
eval_threshold: [0.01, 0.1, 0.2, 0.3, 0.5]
max_entity_pair_distance: null
fixed_relation_types: true  # for eval: only use the given list of relation types (FewRel) for all batches
# fixed_relation_types: false   # for eval: use all relation types of a given batch (DocRED)


name: "large"



```

## File: configs/config_docred.yaml

<a name='file-configs-config_docred.yaml'></a>
*Description*: No specific description available.

```plaintext
# Learning Rate
lr_encoder: 1e-5
lr_others: 1e-4

# Training Parameters
num_steps: 100000
warmup_ratio: 0.1
train_batch_size: 8
eval_every: 300
gradient_accumulation: null
eval_batch_size: 16

# Model Configuration
max_width: 12
model_name: microsoft/deberta-v3-large # hugging face model
fine_tune: true
subtoken_pooling: first
hidden_size: 768
scorer: "dot"
span_mode: marker
refine_prompt: false
refine_relation: false
ffn_mul: 4
dropout: 0.4
scheduler: "cosine_with_warmup"  # "cosine_with_hard_restarts"
loss_func: "binary_cross_entropy_loss"  # "binary_cross_entropy_loss"  # "focal_loss"
# alpha: 0.25
# gamma: 2

# Coreference Resolution
coref_classifier: false
coref_loss_weight: 10.0

# Directory Paths
dataset_name: "docred"
root_dir: ablation_backbone
train_data: "data/docred_train_annotated.jsonl"
eval_data: "data/docred_validation.jsonl"

# "none" if no pretrained model 
prev_path: "none"


# Training Specifics
size_sup: -1
num_train_rel_types: 25   # number of relation labels to use in each given mini-batch
top_k: 1                  # number of relations predictions to return at evaluation time
random_drop: false        # randomly drop relation types
max_len: 512
eval_threshold: 0.0
max_entity_pair_distance: 50
# fixed_relation_types: true  # for eval: only use the given list of relation types (FewRel) for all batches
fixed_relation_types: false   # for eval: use all relation types of a given batch (DocRED)
num_unseen_rel_types: 15      # for eval: will be ignored if `fixed_relation_types` is false

name: "large"



```

## File: configs/config_few_rel.yaml

<a name='file-configs-config_few_rel.yaml'></a>
*Description*: No specific description available.

```plaintext
# Learning Rate
lr_encoder: 1e-5
lr_others: 1e-4
weight_decay_encoder: 0.0
weight_decay_other: 0.0

# Training Parameters
num_steps: 20000
warmup_ratio: 0.1
train_batch_size: 8
eval_every: 300
gradient_accumulation: null
eval_batch_size: 32
num_layers_freeze: null
early_stopping_patience: 12
early_stopping_delta: 0.0
threshold_search_metric: "macro_f1"
max_saves: 1

# Model Configuration
max_width: 12
model_name: microsoft/deberta-v3-large
fine_tune: true
subtoken_pooling: first
hidden_size: 768
scorer: "dot"
rel_mode: marker
span_marker_mode: markerv1
refine_prompt: false
refine_relation: false
ffn_mul: 4
dropout: 0.4
scheduler: "cosine_with_warmup"  # "cosine_with_hard_restarts"
loss_func: "binary_cross_entropy_loss"  # "binary_cross_entropy_loss"  # "focal_loss"
alpha: 0.75
gamma: 3
# add_entity_markers: true
label_embed_strategy: "both"  # "label" "ent_token" "both"


# Coreference Resolution
coref_classifier: false
coref_loss_weight: 10.0
coreference_label: "SELF"

# Directory Paths
dataset_name: "few_rel"
root_dir: ablation_backbone
train_data: "data/few_rel_all.jsonl"
# synthetic_data: "data/zero_rel_all_diff_few_rel.jsonl"

# "none" if no pretrained model 
prev_path: "logs/zero_rel/zero_rel-2024-10-06__21-28-09/saved_at/model_70000"


# Training Specifics
size_sup: -1
num_train_rel_types: 25   # number of relation labels to use in each given mini-batch
num_unseen_rel_types: 15      # for eval: will be ignored if `fixed_relation_types` is false
top_k: 1                  # number of relations predictions to return at evaluation time
random_drop: true       # randomly drop relation types
max_len: 384
eval_threshold: [0.01, 0.1, 0.2, 0.3, 0.5, 0.6]
max_entity_pair_distance: null
fixed_relation_types: true  # for eval: only use the given list of relation types (FewRel) for all batches
# fixed_relation_types: false   # for eval: use all relation types of a given batch (DocRED)


name: "large"



```

## File: configs/config_wiki_zsl.yaml

<a name='file-configs-config_wiki_zsl.yaml'></a>
*Description*: No specific description available.

```plaintext
# Learning Rate
lr_encoder: 1e-5
lr_others: 1e-4
weight_decay_encoder: 0.0
weight_decay_other: 0.0


# Training Parameters
num_steps: 20000
warmup_ratio: 0.1
train_batch_size: 8
eval_every: 300
gradient_accumulation: null  # 4
eval_batch_size: 32
num_layers_freeze: null
early_stopping_patience: 12
early_stopping_delta: 0.0
threshold_search_metric: "macro_f1"
max_saves: 1


# Model Configuration
max_width: 12
model_name: microsoft/deberta-v3-large  # MoritzLaurer/deberta-v3-large-zeroshot-v2.0  # microsoft/deberta-v3-large
fine_tune: true
subtoken_pooling: first   # https://flairnlp.github.io/docs/tutorial-embeddings/transformer-embeddings#arguments
hidden_size: 768
scorer: "dot"
rel_mode: marker
span_marker_mode: markerv1
refine_prompt: false
refine_relation: false
ffn_mul: 4
dropout: 0.4
scheduler: "cosine_with_warmup"  # "cosine_with_hard_restarts"
loss_func: "binary_cross_entropy_loss" # "binary_cross_entropy_loss"  # "focal_loss"
alpha: 0.3
gamma: 3
# add_entity_markers: true
label_embed_strategy: "both"  # "label" "ent_token" "both"


# Coreference Resolution
coref_classifier: false
coref_loss_weight: 10.0
coreference_label: "SELF"

# Directory Paths
dataset_name: "wiki_zsl"
root_dir: ablation_backbone
train_data: "data/wiki_zsl_all.jsonl"
# synthetic_data: "data/zero_rel_all_diff_wiki_zsl.jsonl"

# "none" if no pretrained model 
prev_path: "logs/zero_rel/zero_rel-2024-10-06__21-28-09/saved_at/model_70000"


# Training Specifics
size_sup: -1
num_train_rel_types: 25   # number of relation labels to use in each given mini-batch
num_unseen_rel_types: 15
top_k: 1                  # number of relations predictions to return at evaluation time
random_drop: true       # randomly drop relation types
max_len: 512
eval_threshold: [0.01, 0.1, 0.2, 0.3, 0.5, 0.6]
max_entity_pair_distance: null
fixed_relation_types: true  # for eval: only use the given list of relation types (FewRel) for all batches
# fixed_relation_types: false   # for eval: use all relation types of a given batch (DocRED)


name: "large"



```

