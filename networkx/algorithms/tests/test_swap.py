import pytest
import networkx as nx

# import random
# random.seed(0)


def test_double_edge_swap():
    graph = nx.barabasi_albert_graph(200, 1)
    degrees = sorted(d for n, d in graph.degree())
    G = nx.double_edge_swap(graph, 40)
    assert degrees == sorted(d for n, d in graph.degree())


def test_double_edge_swap_seed():
    graph = nx.barabasi_albert_graph(200, 1)
    degrees = sorted(d for n, d in graph.degree())
    G = nx.double_edge_swap(graph, 40, seed=1)
    assert degrees == sorted(d for n, d in graph.degree())


def test_connected_double_edge_swap():
    graph = nx.barabasi_albert_graph(200, 1)
    degrees = sorted(d for n, d in graph.degree())
    G = nx.connected_double_edge_swap(graph, 40, seed=1)
    assert nx.is_connected(graph)
    assert degrees == sorted(d for n, d in graph.degree())

#def test_connected_double_edge_swap2(): ##NEW
#    graph = nx.barabasi_albert_graph(200, 1)
#    degrees = sorted(d for n, d in graph.degree())
#    G = nx.connected_double_edge_swap(graph, 40, _window_threshold=0, seed=1)
#    assert nx.is_connected(graph)
#    assert degrees == sorted(d for n, d in graph.degree())

def test_double_edge_swap_small():
    with pytest.raises(nx.NetworkXError):
        G = nx.double_edge_swap(nx.path_graph(3))


def test_double_edge_swap_tries():
    with pytest.raises(nx.NetworkXError):
        G = nx.double_edge_swap(nx.path_graph(10), nswap=1, max_tries=0)

##NEW
def test_double_edge_directed():
    graph = nx.DiGraph([(0, 1), (2, 3)])
    with pytest.raises(nx.NetworkXError):
        G = nx.double_edge_swap(graph)

##NEW
#def test_double_edge_max_tries():
#    with pytest.raises(nx.NetworkXAlgorithmError):
#        G = nx.double_edge_swap(nx.path_graph(4), nswap=1, max_tries=5)


def test_connected_double_edge_swap_small():
    with pytest.raises(nx.NetworkXError):
        G = nx.connected_double_edge_swap(nx.path_graph(3))


def test_connected_double_edge_swap_not_connected():
    with pytest.raises(nx.NetworkXError):
        G = nx.path_graph(3)
        nx.add_path(G, [10, 11, 12])
        G = nx.connected_double_edge_swap(G)


def test_degree_seq_c4():
    G = nx.cycle_graph(4)
    degrees = sorted(d for n, d in G.degree())
    G = nx.double_edge_swap(G, 1, 100)
    assert degrees == sorted(d for n, d in G.degree())
