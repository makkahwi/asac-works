import pytest
from graph.graph import Graph

# Required Tests ######################################################################

# 1. Node can be successfully added to the graph
def test_add_vertex():
    graph = Graph()

    actual = graph.add_vertex("Node A").value
    expected = "Node A"
    assert actual == expected


# 2. An edge can be successfully added to the graph
def test_add_edge(graph1):
    graph1.add_edge("Node E", "Node F")

    actual = graph1.adj_list["Node E"].edges
    expected = ["Node B", "Node F"]
    assert actual == expected


# 3. A collection of all nodes can be properly retrieved from the graph
def test_get_nodes(graph1):
    actual = graph1.get_nodes()
    expected = ["Node A", "Node B", "Node C", "Node D", "Node E", "Node F"]
    assert actual == expected


# 4. All appropriate neighbours can be retrieved from the graph
def test_get_neighbours(graph1):
    actual = graph1.get_neighbours("Node A")
    expected = ["Node B", "Node C"]
    assert actual == expected


# 5. neighbours are returned with the weight between nodes included
def test_get_weighted_neighbours(graph2):
    actual = graph2.get_neighbours("Node A")
    expected = [("Node B", 5), ("Node C", 6)]
    assert actual == expected


# 6. The proper size is returned, representing the number of nodes in the graph
def test_size(graph2):
    actual = graph2.size()
    expected = 4
    assert actual == expected


# 7. A graph with only one node and edge can be properly returned
def test_get_neighbours_empty(graph3):
    actual = graph3.get_nodes()
    expected = ["Node A"]
    assert actual == expected


# Edge Case: Empty graph in “Size”
# 8. An empty graph properly returns null
def test_empty_graph_size():
    graph = Graph()

    actual = graph.size()
    expected = None
    assert actual == expected


# Edge Case Tests ######################################################################

# Input none in “Add Vertex”
def test_add_none_vertex():
    graph = Graph()

    with pytest.raises(Exception):
        graph.add_vertex(None)


# Any or both input of 2 vertices in “Add Edge” doesn’t exist in graph.
def test_add_edge_for_non_existing_vertex(graph1):
    with pytest.raises(Exception):
        graph1.add_edge("Node F", "Node G")


# Input weight in “Add Edge” isn’t numerical
def test_add_edge_with_wrong_weight(graph1):
    with pytest.raises(Exception):
        graph1.add_edge("Node F", "Node G", "Edge")


@pytest.fixture
def graph1():
    graph1 = Graph()
    graph1.add_vertex("Node A")
    graph1.add_vertex("Node B")
    graph1.add_vertex("Node C")
    graph1.add_vertex("Node D")
    graph1.add_vertex("Node E")
    graph1.add_vertex("Node F")
    graph1.add_edge("Node A", "Node B")
    graph1.add_edge("Node A", "Node C")
    graph1.add_edge("Node B", "Node D")
    graph1.add_edge("Node B", "Node E")
    graph1.add_edge("Node C", "Node D")
    graph1.add_edge("Node D", "Node F")

    # Graph Representation
    # Node A ----- Node B ----- Node E
    #   |             |
    #   |             |
    # Node C ----- Node D ----- Node F

    return graph1


@pytest.fixture
def graph2():
    graph2 = Graph()
    graph2.add_vertex("Node A")
    graph2.add_vertex("Node B")
    graph2.add_vertex("Node C")
    graph2.add_vertex("Node D")
    graph2.add_edge("Node A", "Node B", 5)
    graph2.add_edge("Node A", "Node C", 6)
    graph2.add_edge("Node B", "Node D", 7)
    graph2.add_edge("Node C", "Node D", 8)

    # Graph Representation
    # Node A --5-- Node B
    #   |             |
    #   6             7
    #   |             |
    # Node C --8-- Node D

    return graph2


@pytest.fixture
def graph3():
    graph3 = Graph()
    graph3.add_vertex("Node A")
    return graph3
