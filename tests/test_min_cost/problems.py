from dataclasses import dataclass

from flowprog.graph_objects import CapacitatedCostEdge, Graph, Node


@dataclass
class MinCostProblem:
    graph: Graph
    source: Node
    sink: Node
    flow: float
    min_cost: float
    # TODO: add in residual graph


def get_problem_b() -> MinCostProblem:
    source_node = Node("source")
    sink_node = Node("sink")

    node_a = Node("node_a")
    node_b = Node("node_b")
   
    edge_source_a = CapacitatedCostEdge((source_node, node_a), capacity=2, cost=4)
    edge_source_b = CapacitatedCostEdge((source_node, node_b), capacity=2, cost=1)

    edge_a_b = CapacitatedCostEdge((node_a, node_b), capacity=1, cost=1)
    edge_b_a = CapacitatedCostEdge((node_b, node_a), capacity=1, cost=3)

    edge_a_sink = CapacitatedCostEdge((node_a, sink_node), capacity=1, cost=5)
    edge_b_sink = CapacitatedCostEdge((node_b, sink_node), capacity=1, cost=2)

    edge_list = [
        edge_source_a,
        edge_source_b,
        edge_a_b,
        edge_b_a,
        edge_a_sink,
        edge_b_sink,
    ]

    graph = Graph(edge_list)
    flow = 2
    min_cost = 12

    return MinCostProblem(
        graph,
        source_node,
        sink_node,
        flow,
        min_cost,
    )


PROBLEMS = [get_problem_b()]
