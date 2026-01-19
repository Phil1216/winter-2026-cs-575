from network_utilities import adjacency_list_to_graph
import networkx as nx
import numpy as np
import plotting_utilities as pu

def test_homework_problem_7() -> None:
    # What I expect
    desired_number_nodes: int = 6
    desired_number_edges = 10
    desired_max_degree = 5
    desired_median_degree = 3

    # when
    ### FIX THIS ADJACENCY LIST
    adjacency_list: dict[int, set[int]] = {1: {2, 5, 6},
                                           2: {3, 1, 5, 4},
                                           3: {4, 2, 5},
                                           4: {5, 3, 2},
                                           5: {1, 4, 6, 2, 3},
                                           6: {5, 1}}
    G = adjacency_list_to_graph(adjacency_list)
    degree_list: list[int] = [y for (_,y) in G.degree]

    # pu.show_graph(G)

    # then
    assert nx.is_connected(G)
    assert len(G.nodes()) == desired_number_nodes
    assert len(G.edges) == desired_number_edges
    assert max(degree_list) == desired_max_degree
    assert np.median(degree_list) == desired_median_degree