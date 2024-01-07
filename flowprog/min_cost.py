from functools import reduce
from typing import Tuple


from flowprog.graph_objects import CapacitatedCostEdge, Edge, Graph, Node
from flowprog.max_flow import EdmonsKarpAlgorithm
from flowprog.path_finding import BreadthFirstSearch
from flowprog.shortest_path import FloydWarshallAlgorithm


def min_cost_edge_cond(edge: CapacitatedCostEdge):
    # check if edge is at capacity
    return edge.remaining_capacity > 0


class MinCostBFS(BreadthFirstSearch):
    @staticmethod
    def _edge_cond(edge: Edge) -> bool:
        return min_cost_edge_cond(edge)

    @staticmethod
    def _edge_constructor(from_node: Node, to_node: Node) -> CapacitatedCostEdge:
        return CapacitatedCostEdge((from_node, to_node), 0, 0, -1)


class MinCostFloydWarshallAlgorithm(FloydWarshallAlgorithm):
    @staticmethod
    def _edge_cond(edge: Edge) -> bool:
        return min_cost_edge_cond(edge)


class CycleCancelingAlgorithm:
    def __init__(self) -> None:
        self.find_path = MinCostBFS()
        self.negative_cost_cycle_indentifier = MinCostFloydWarshallAlgorithm()
        self.find_max_flow = EdmonsKarpAlgorithm()

    def __call__(
        self, graph: Graph, source: Node, sink: Node, flow: float
    ) -> Tuple[float, Graph]:
        current_flow = 0.0
        current_cost = 0.0

        # build incremental flow network
        # find flow of required amount
        current_flow, min_cost_flow_network = self.find_max_flow(
            graph, source, sink, max_flow=flow
        )
        current_cost = sum(
            [edge.cost * edge.flow for edge in min_cost_flow_network.edges]
        )

        incremental_flow_network = Graph()
        # add back arcs
        for edge in reduce(
            lambda x1, x2: x1 + x2, min_cost_flow_network.edge_list.values()
        ):
            forward_edge = CapacitatedCostEdge(
                edge.nodes,
                capacity=edge.capacity - edge.flow,
                cost=edge.cost,
                is_back_edge=False,
            )
            # add reverse arcs to graph
            backward_edge = CapacitatedCostEdge(
                edge.nodes[::-1],
                capacity=edge.flow,
                cost=-1 * edge.cost,
                is_back_edge=True,
            )
            incremental_flow_network.add_edge(forward_edge)
            incremental_flow_network.add_edge(backward_edge)

        while True:
            # remove negative cycles
            self.negative_cost_cycle_indentifier(incremental_flow_network)
            negative_cost_cycles_nodes = (
                self.negative_cost_cycle_indentifier.get_negative_cycles()
            )
            negative_cost_cycles_edges = []

            if len(negative_cost_cycles_nodes) == 0:
                break

            # get edges of cycles
            for node_cycle in negative_cost_cycles_nodes:
                edge_cycle = []
                for i, from_node in enumerate(node_cycle):
                    to_node = node_cycle[(i + 1) % len(node_cycle)]
                    for edge in incremental_flow_network.edge_list[from_node]:
                        if edge.nodes[-1] == to_node and min_cost_edge_cond(edge):
                            edge_cycle.append(edge)
                negative_cost_cycles_edges.append(edge_cycle)

            # remove cycle from incremental network and update flow network
            for edge_cycle in negative_cost_cycles_edges:
                # flow to push around cycle
                cycle_capacity = min([edge.remaining_capacity for edge in edge_cycle])
                cycle_cost = cycle_capacity * sum([edge.cost for edge in edge_cycle])

                for edge in edge_cycle:
                    # update edge flow in incremental network
                    edge.flow += cycle_capacity

                    # update flow of corresponding edge in flow network
                    for flow_edge in min_cost_flow_network.edges:
                        if edge.nodes == flow_edge.nodes:  # augment flow
                            flow_edge.flow += cycle_capacity
                            break
                        if edge.nodes[::-1] == flow_edge.nodes:  # recind flow
                            flow_edge.flow -= cycle_capacity
                            break

                current_cost += cycle_cost

        return current_cost, min_cost_flow_network


class SuccessiveShortestPathAlgorithm:
    pass
