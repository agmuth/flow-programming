from typing import Any
from flowprog.graph import Graph, Node, Edge
from collections import dequeue, defaultdict
from typing import Tuple, Iterable, Any


class BreadthFirstSearch:
    def __init__(self) -> None:
        self.search_dequeue = dequeue()
        self.visited_nodes = defaultdict(False)
        
    def _add_node_to_search_dequeue(self, edge: Edge) -> None:
        self.search_dequeue.append(Edge)
        
    def _get_edge_from_search_dequeue(self) -> Tuple[Node, Node]:
        return self.search_dequeue.popLeft()
        
    def _reconstruct_path(self, start: Node, end: Node) -> Iterable[Any]:
        pass
    
    def __call__(self, graph: Graph, start: Node, end: Node) -> Any:
        self._add_edge_to_queue(Edge((None, start)))
        
        while len(self.search_dequeue) > 0:
            edge_to_search_along = self._get_node_from_search_dequeue()
            next_node = edge_to_search_along.nodes[1]
            
            if next_node == end:
                break
            if self.visited_nodes[next_node]:
                continue
            
            self.visited_nodes[next_node] = True
            for edge in graph.edge_list[next_node]:
                self._add_edge_to_search_dequeue(edge)
                
        else:
            return list()  # no path
        
        return self._reconstruct_path(start, end)
            
            
            
            
        
    


if __name__ == "__main__":
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
    
    edge_list = [
        edge_a_b,
        edge_a_c,
        edge_b_d,
        edge_b_e,
        edge_c_f,
        edge_c_g,
        edge_d_h,
    ]
    
    graph = Graph(edge_list)
    bfs = BreadthFirstSearch()
    bfs(graph)
    
    