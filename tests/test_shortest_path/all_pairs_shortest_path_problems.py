from dataclasses import dataclass

from flowprog.graph_objects import Graph, Node, WeightedEdge


@dataclass
class AllPairsShortestPathProblem:
    graph: Graph
    shortest_paths: dict  # TypedDict[Node, TypedDict[Node, float]]


def get_problem_1() -> AllPairsShortestPathProblem:
    # ref https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
    node_1 = Node(name="1")
    node_2 = Node(name="2")
    node_3 = Node(name="3")
    node_4 = Node(name="4")

    edge_1_3 = WeightedEdge((node_1, node_3), -2)
    edge_2_1 = WeightedEdge((node_2, node_1), 4)
    edge_2_3 = WeightedEdge((node_2, node_3), 3)
    edge_3_4 = WeightedEdge((node_3, node_4), 2)
    edge_4_2 = WeightedEdge((node_4, node_2), -1)

    edge_list = [
        # (!) ordering here is important
        edge_1_3,
        edge_2_1,
        edge_2_3,
        edge_3_4,
        edge_4_2,
    ]

    graph = Graph(edge_list)
    shortest_paths = {
        node_1: {
            node_1: 0,
            node_2: -1,
            node_3: -2,
            node_4: 0,
        },
        node_2: {
            node_1: 4,
            node_2: 0,
            node_3: 2,
            node_4: 4,
        },
        node_3: {
            node_1: 5,
            node_2: 1,
            node_3: 0,
            node_4: 2,
        },
        node_4: {
            node_1: 3,
            node_2: -1,
            node_3: 1,
            node_4: 0,
        },
    }

    return AllPairsShortestPathProblem(graph, shortest_paths)


PROBLEMS = [get_problem_1()]
