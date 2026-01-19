from network_utilities import adjacency_list_to_graph
import networkx as nx
import plotting_utilities as pu

def test_homework_problem_8() -> None:
    # What I expect
    desired_number_nodes: int = 6
    desired_minimum_density: float = 0.21
    desired_maximum_density: float = 0.23

    # when
    ## FIX THIS ADJACENCY LIST
    adjacency_list: dict[int, set[int]] = {1: {4, 5},
                                           2: {3, 7},
                                           3: {4, 2, 6},
                                           4: {3, 1},
                                           5: {1},
                                           6: {3, 8},
                                           7: {2},
                                           8: {6, 9},
                                           9: {8}}
    G = adjacency_list_to_graph(adjacency_list)

    # pu.show_graph(G)

    # then
    assert nx.is_connected(G)
    assert len(G.nodes()) >= desired_number_nodes
    assert nx.density(G) >= desired_minimum_density
    assert nx.density(G) <= desired_maximum_density