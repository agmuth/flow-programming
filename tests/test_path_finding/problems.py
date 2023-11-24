from dataclasses import dataclass
from typing import Optional

from flowprog.graph_objects import Edge, Graph, Node, NodePath


@dataclass
class PathFindingProblem:
    graph: Graph
    start: Node
    end: Node
    bfs_path: Optional[NodePath] = None
    dfs_path: Optional[NodePath] = None


def get_problem_1() -> PathFindingProblem:
    node_a = Node(name="a")
    node_b = Node(name="b")
    node_c = Node(name="c")
    node_d = Node(name="d")
    node_e = Node(name="e")
    node_f = Node(name="f")
    node_g = Node(name="g")
    node_h = Node(name="h")

    edge_a_b = Edge((node_a, node_b))
    edge_a_c = Edge((node_a, node_c))

    edge_b_d = Edge((node_b, node_d))
    edge_b_e = Edge((node_b, node_e))

    edge_c_f = Edge((node_c, node_f))
    edge_c_g = Edge((node_c, node_g))

    edge_d_h = Edge((node_d, node_h))
    edge_g_h = Edge((node_g, node_h))

    edge_list = [
        # (!) ordering here is important
        edge_a_b,
        edge_a_c,
        edge_b_d,
        edge_b_e,
        edge_c_f,
        edge_c_g,
        edge_d_h,
        edge_g_h,
    ]

    graph = Graph(edge_list)
    start = node_a
    end = node_h
    bfs_path = NodePath([node_a, node_b, node_d, node_h])
    dfs_path = NodePath([node_a, node_c, node_g, node_h])

    return PathFindingProblem(
        graph,
        start,
        end,
        bfs_path,
        dfs_path,
    )


PROBLEMS = [get_problem_1()]
