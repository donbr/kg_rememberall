import networkx as nx
from rdflib import Graph
from pyvis.network import Network
import json


def create_graph(nodes, edges, node_attributes=None, edge_attributes=None, directed=True) -> nx.Graph:
    """
    Creates a NetworkX graph from a list of nodes and edges.

    Args:
        nodes (list): List of node identifiers.
        edges (list): List of tuples representing edges between nodes.
        node_attributes (dict, optional): Dictionary of attributes for nodes.
        edge_attributes (dict, optional): Dictionary of attributes for edges.
        directed (bool, optional): If True, creates a directed graph. Defaults to True.

    Returns:
        nx.Graph: The created NetworkX graph.
    """
    graph = nx.DiGraph() if directed else nx.Graph()

    for node in nodes:
        attrs = node_attributes.get(node, {}) if node_attributes else {}
        graph.add_node(node, **attrs)

    for edge in edges:
        attrs = edge_attributes.get(edge, {}) if edge_attributes else {}
        graph.add_edge(*edge, **attrs)

    return graph

def create_graph_using_dict(sections, subsections, color_scheme):
    """
    Create a NetworkX graph for an Arxiv paper structure.
    
    Args:
        sections (dict): Dictionary of sections with their properties.
        subsections (dict): Dictionary of subsections with their properties.
        color_scheme (dict): Color scheme for nodes (e.g., {"section": "lightblue", "subsection": "lightgreen"}).
    
    Returns:
        nx.DiGraph: A directed graph representing the paper structure.
    """
    graph = nx.DiGraph()

    # Add nodes for sections
    for section, properties in sections.items():
        graph.add_node(section, **properties)
    section_keys = list(sections.keys())

    # Add edges between sections
    for i in range(len(section_keys) - 1):
        graph.add_edge(section_keys[i], section_keys[i + 1], transition_summary=f"Transition from {section_keys[i]} to {section_keys[i + 1]}.")

    # Add subsections
    for section, subs in subsections.items():
        for sub, properties in subs:
            graph.add_node(sub, **properties)
            graph.add_edge(section, sub, transition_summary=f"Transition from {section} to {sub}.")

    return graph


def import_ontology_as_graph(ontology_file: str, format: str = "turtle") -> nx.MultiDiGraph:
    """
    Parses an RDF/OWL ontology file and creates a NetworkX graph.

    Args:
        ontology_file (str): Path to the ontology file.
        format (str, optional): Format of the ontology file (e.g., "turtle", "xml"). Defaults to "turtle".

    Returns:
        nx.MultiDiGraph: A directed graph representing the ontology.
    """
    rdf_graph = Graph()
    rdf_graph.parse(ontology_file, format=format)

    nx_graph = nx.MultiDiGraph()

    for s, p, o in rdf_graph:
        nx_graph.add_node(str(s), type="resource")
        nx_graph.add_node(str(o), type="resource")
        nx_graph.add_edge(str(s), str(o), predicate=str(p))

    return nx_graph


def visualize_with_pyvis(graph: nx.Graph, output_file="graph.html", notebook=True, physics=True, node_size=15):
    """
    Visualizes a NetworkX graph using PyVis.

    Args:
        graph (nx.Graph): The NetworkX graph to visualize.
        output_file (str): Path to save the HTML visualization.
        notebook (bool): If True, renders the graph in a Jupyter notebook.
        physics (bool): If True, enables physics for the graph layout. Defaults to True.
        node_size (int): Size of the nodes in the visualization. Defaults to 15.

    Returns:
        None
    """
    net = Network(notebook=notebook, directed=nx.is_directed(graph))

    for node, data in graph.nodes(data=True):
        net.add_node(node, label=node, size=node_size, **data)

    for source, target, data in graph.edges(data=True):
        net.add_edge(source, target, **data)

    net.toggle_physics(physics)
    net.show(output_file)


def export_to_graphml(graph: nx.Graph, filename: str):
    """
    Exports a NetworkX graph to GraphML format.

    Args:
        graph (nx.Graph): The NetworkX graph to export.
        filename (str): Path to save the GraphML file.

    Returns:
        None
    """
    nx.write_graphml(graph, filename)


def export_to_json(graph: nx.Graph, filename: str):
    """
    Exports a NetworkX graph to JSON format.

    Args:
        graph (nx.Graph): The NetworkX graph to export.
        filename (str): Path to save the JSON file.

    Returns:
        None
    """
    data = nx.node_link_data(graph, edges="edges")
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def query_graph(graph: nx.Graph, query: str) -> list:
    """
    Queries a NetworkX graph using a custom filter function.

    Args:
        graph (nx.Graph): The NetworkX graph to query.
        query (str): A string that evaluates to a boolean expression for filtering nodes or edges.

    Returns:
        list: A list of nodes or edges matching the query.
    """
    results = []
    for node, data in graph.nodes(data=True):
        if eval(query, {"__builtins__": {}}, data):
            results.append((node, data))
    return results
