from dataclasses import dataclass

from flowprog.graph_objects import CapacitatedEdge, Graph, Node


@dataclass
class MaxFlowProblem:
    graph: Graph
    source: Node
    sink: Node
    max_flow: float
    # TODO: add in residual graph


def get_problem_1() -> MaxFlowProblem:
    source_node = Node("source")
    sink_node = Node("sink")

    node_0 = Node("node_0")
    node_1 = Node("node_1")
    node_2 = Node("node_2")
    node_3 = Node("node_3")

    edge_source_0 = CapacitatedEdge((source_node, node_0), 10)
    edge_source_1 = CapacitatedEdge((source_node, node_1), 10)

    edge_0_2 = CapacitatedEdge((node_0, node_2), 15)
    edge_1_3 = CapacitatedEdge((node_1, node_3), 10)
    edge_3_0 = CapacitatedEdge((node_3, node_0), 5)

    edge_2_sink = CapacitatedEdge((node_2, sink_node), 15)
    edge_3_sink = CapacitatedEdge((node_3, sink_node), 5)

    edge_list = [
        edge_source_0,
        edge_source_1,
        edge_0_2,
        edge_1_3,
        edge_3_0,
        edge_2_sink,
        edge_3_sink,
    ]

    graph = Graph(edge_list)
    max_flow = 20

    return MaxFlowProblem(
        graph,
        source_node,
        sink_node,
        max_flow,
    )


PROBLEMS = [get_problem_1()]
