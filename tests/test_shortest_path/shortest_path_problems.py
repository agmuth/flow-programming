from dataclasses import dataclass

from flowprog.graph_objects import Graph, Node, NodePath, WeightedEdge


@dataclass
class ShortestPathProblem:
    graph: Graph
    start: Node
    end: Node
    shortest_path: NodePath


def get_problem_1() -> ShortestPathProblem:
    node_a = Node(name="a")
    node_b = Node(name="b")
    node_c = Node(name="c")
    node_d = Node(name="d")
    node_e = Node(name="e")

    edge_a_b = WeightedEdge((node_a, node_b), 4)
    edge_a_c = WeightedEdge((node_a, node_c), 1)
    edge_c_b = WeightedEdge((node_c, node_b), 2)
    edge_b_d = WeightedEdge((node_b, node_d), 1)
    edge_c_d = WeightedEdge((node_c, node_d), 5)
    edge_d_e = WeightedEdge((node_d, node_e), 3)

    edge_list = [
        # (!) ordering here is important
        edge_a_b,
        edge_a_c,
        edge_c_b,
        edge_b_d,
        edge_c_d,
        edge_d_e,
    ]

    graph = Graph(edge_list)
    shortest_path = NodePath([node_a, node_c, node_b, node_d, node_e])
    return ShortestPathProblem(graph, node_a, node_e, shortest_path)


PROBLEMS = [get_problem_1()]
