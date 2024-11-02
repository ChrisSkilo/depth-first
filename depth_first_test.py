import pytest
from graph import Graph  

@pytest.fixture
def setup_graph():
    graph = Graph()
    graph.add_node("Jasmine")
    graph.add_node("Ada")
    graph.add_node("Lydia")
    graph.add_node("Rose")
    graph.add_node("Dylan")
    graph.add_node("Allison")
    graph.add_node("Thomas")
    graph.add_node("Sarah")
    graph.create_edge("Jasmine", "Ada")
    graph.create_edge("Jasmine", "Lydia")
    graph.create_edge("Jasmine", "Rose")
    graph.create_edge("Ada", "Dylan")
    graph.create_edge("Lydia", "Ada")
    graph.create_edge("Dylan", "Allison")
    graph.create_edge("Lydia", "Thomas")
    return graph

def test_depth_first_reachable_target_not_exist(setup_graph):
    graph = setup_graph
    result = graph.depth_first_reachable("Jasmine", "Albert")
    assert result == False

def test_depth_first_reachable_starting_not_exist(setup_graph):
    graph = setup_graph
    result = graph.depth_first_reachable("Albert", "Thomas")
    assert result == False

def test_depth_first_reachable_first_friend(setup_graph):
    graph = setup_graph
    result = graph.depth_first_reachable("Jasmine", "Ada")
    assert result == True

def test_depth_first_reachable_false(setup_graph):
    graph = setup_graph
    result = graph.depth_first_reachable("Jasmine", "Sarah")
    assert result == False