from dataclasses import dataclass
from typing import List

from flowprog.graph_objects import Graph, Node, NodePath, WeightedEdge


@dataclass
class NegativeCycleProblem:
    graph: Graph
    negative_cycles: List[NodePath]


def get_problem_1() -> NegativeCycleProblem:
    node_a = Node(name="a")
    node_b = Node(name="b")
    node_c = Node(name="c")
    node_d = Node(name="d")
    node_e = Node(name="e")
    node_f = Node(name="f")
    node_g = Node(name="g")

    # negative cycles
    edge_a_b = WeightedEdge((node_a, node_b), -2)
    edge_b_a = WeightedEdge((node_b, node_a), -2)

    edge_d_e = WeightedEdge((node_d, node_e), -2)
    edge_e_d = WeightedEdge((node_e, node_d), -2)

    # connect negative cycle to node not in negative cycle
    node_b_c = WeightedEdge((node_b, node_c), 1)
    node_d_c = WeightedEdge((node_d, node_c), 1)

    # positive cycle
    node_c_f = WeightedEdge((node_c, node_f), 1)
    node_f_g = WeightedEdge((node_f, node_g), 1)
    node_g_c = WeightedEdge((node_g, node_c), 2)

    edge_list = [
        # (!) ordering here is important
        edge_a_b,
        edge_b_a,
        edge_d_e,
        edge_e_d,
        node_b_c,
        node_d_c,
        node_c_f,
        node_f_g,
        node_g_c,
    ]

    graph = Graph(edge_list)
    negative_cycles = [
        [node_a, node_b],
        [node_d, node_e],
    ]

    return NegativeCycleProblem(graph, negative_cycles)


PROBLEMS = [get_problem_1()]
