from copy import deepcopy
from functools import reduce
from typing import Tuple

import numpy as np

from flowprog.graph_objects import CapacitatedEdge, Edge, Graph, Node
from flowprog.path_finding import BreadthFirstSearch, DepthFirstSearch


def max_flow_edge_cond(edge: CapacitatedEdge):
    # check if edge is at capacity
    return edge.is_residual or edge.remaining_capacity > 0


class MaxFlowDFS(DepthFirstSearch):
    @staticmethod
    def _edge_cond(edge: Edge) -> bool:
        return max_flow_edge_cond(edge)

    @staticmethod
    def _edge_constructor(from_node: Node, to_node: Node) -> CapacitatedEdge:
        return CapacitatedEdge((from_node, to_node), np.Inf, 0)


class MaxFlowBFS(BreadthFirstSearch):
    @staticmethod
    def _edge_cond(edge: Edge) -> bool:
        return max_flow_edge_cond(edge)

    @staticmethod
    def _edge_constructor(from_node: Node, to_node: Node) -> CapacitatedEdge:
        return CapacitatedEdge((from_node, to_node), np.Inf, 0)


class FordFulkersonAlgorithm:
    def __init__(self) -> None:
        self.find_path = MaxFlowDFS()

    def __call__(self, graph: Graph, source: Node, sink: Node) -> Tuple[float, Graph]:
        max_flow = 0.0
        residual_graph = deepcopy(graph)
        for edge in reduce(lambda x1, x2: x1 + x2, residual_graph.edge_list.values()):
            # add reverse arcs to graph
            residual_edge = CapacitatedEdge(edge.nodes[::-1], 0.0, 0.0)
            residual_graph.add_edge(residual_edge)

        while True:
            augmenting_path_nodes = self.find_path(residual_graph, source, sink)

            if len(augmenting_path_nodes) == 0:
                break  # optimal soln found

            augmenting_path_edges = residual_graph.get_edge_path(augmenting_path_nodes)
            augmenting_flow = min([edge.capacity for edge in augmenting_path_edges])
            max_flow += augmenting_flow

            for augmenting_edge in augmenting_path_edges:
                for i, edge in enumerate(
                    residual_graph.edge_list[augmenting_edge.nodes[0]]
                ):
                    if augmenting_edge.nodes[1] == edge.nodes[1]:
                        residual_graph.edge_list[augmenting_edge.nodes[0]][
                            i
                        ].augment_flow(augmenting_flow)

        # remove backward arcs from residual graph
        for edge in reduce(lambda x1, x2: x1 + x2, residual_graph.edge_list.values()):
            if edge.is_residual:
                residual_graph.remove_edge(edge)

        return max_flow, residual_graph


class EdmonsKarpAlgorithm(FordFulkersonAlgorithm):
    def __init__(self) -> None:
        self.find_path = MaxFlowBFS()
