from flowprog.graph_objects import Edge, Node, Graph, CapacitatedEdge
from functools import reduce
from flowprog.path_finding import DepthFirstSearch, BreadthFirstSearch
from copy import deepcopy
from typing import Tuple
import numpy as np

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
        for edge in reduce(lambda x1, x2: x1+x2, residual_graph.edge_list.values()):
            # add reverse arcs to graph
            residual_edge = CapacitatedEdge(edge.nodes[::-1], 0.0, 0.0)
            residual_graph.add_edge(residual_edge)
        
        while True:
            augmenting_path_nodes = self.find_path(residual_graph, source, sink)
            
            if len(augmenting_path_nodes) == 0:
                break # optimal soln found
            
            augmenting_path_edges =  residual_graph.get_edge_path(augmenting_path_nodes)
            augmenting_flow = min([edge.capacity for edge in augmenting_path_edges])
            max_flow += augmenting_flow
            
            for augmenting_edge in augmenting_path_edges:
                for i, edge in enumerate(residual_graph.edge_list[augmenting_edge.nodes[0]]):
                    if augmenting_edge.nodes[1] == edge.nodes[1]:
                        residual_graph.edge_list[augmenting_edge.nodes[0]][i].augment_flow(augmenting_flow)
            else:
                pass
            
        # remove backward arcs from residual graph
        for edge in reduce(lambda x1, x2: x1+x2, residual_graph.edge_list.values()):
            if edge.is_residual:
                residual_graph.remove_edge(edge)
                
        return max_flow, residual_graph
           
        
        
        
class EdmonsKarpAlgorithm(FordFulkersonAlgorithm):
    def __init__(self) -> None:
        self.find_path = MaxFlowBFS()




if __name__ == "__main__":
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
    ford_fulkerson_alg = FordFulkersonAlgorithm()
    ford_fulkerson_alg(graph, source_node, sink_node)