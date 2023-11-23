from collections import defaultdict, deque
from typing import Any, Iterable, Tuple
from queue import PriorityQueue
import numpy as np

from flowprog.graph import Edge, Graph, Node


class BreadthFirstSearch:
    def __init__(self) -> None:
        self.search_deque = deque()
        self.visited_nodes = defaultdict(lambda: False)
        self.prev_node_mapping = defaultdict(None)

    def _add_edge_to_search_deque(self, edge: Edge) -> None:
        self.search_deque.append(edge)

    def _get_edge_from_search_deque(self) -> Edge:
        # FIFO
        return self.search_deque.popleft()

    def _reconstruct_path(self, start: Node, end: Node) -> Iterable[Node]:
        path = [end]
        while path[-1] != start:
            path.append(self.prev_node_mapping[path[-1]])
        return path[::-1]

    def __call__(self, graph: Graph, start: Node, end: Node) -> Any:
        self._add_edge_to_search_deque(Edge((None, start)))

        while len(self.search_deque) > 0:
            edge_to_search_along = self._get_edge_from_search_deque()
            prev_node, curr_node = edge_to_search_along.nodes

            if self.visited_nodes[curr_node]:
                continue

            self.visited_nodes[curr_node] = True
            self.prev_node_mapping[curr_node] = prev_node

            if curr_node == end:
                break

            for edge in graph.edge_list[curr_node]:
                self._add_edge_to_search_deque(edge)

        else:
            return list()  # no path

        return self._reconstruct_path(start, end)


class DepthFirstSearch(BreadthFirstSearch):
    def _get_edge_from_search_deque(self) -> Edge:
        # LIFO
        return self.search_deque.pop()


class PriorityFirstSearch:
    def __init__(self) -> None:
        self.search_pqueue = PriorityQueue()
        self.visited_nodes = defaultdict(lambda: False)
        self.prev_node_mapping = defaultdict(None)
        self.node_dist = defaultdict(lambda _: np.Inf)
        
    
    def _add_node_to_search_pqueue(self, node: Node) -> None:
        dist = self.node_dist[node]
        self.search_pqueue.put((node, dist))

    def _get_node_from_search_pqueue(self) -> Node:
        return self.search_pqueue.get()

    def _reconstruct_path(self, start: Node, end: Node) -> Iterable[Node]:
        path = [end]
        while path[-1] != start:
            path.append(self.prev_node_mapping[path[-1]])
        return path[::-1]
    
    def __call__(self, graph: Graph, start: Node, end: Node) -> Any:
        reached_end_node = False
        self.node_dist[start] = 0
        self._add_node_to_search_pqueue(start)
        
        while len(self.search_pqueue) > 0:
            node_curr, dist_curr = self._get_node_from_search_pqueue()
            for edge in graph.edge_list[node_curr]:
                node_next = edge.nodes[1]
                dist_next = edge.weight + dist_curr
                if dist_next < self.node_dist[node_next]:
                    # found a shorter path to `node_next`
                    self.node_dist[node_next] = dist_next
                    self.prev_node_mapping[node_next] = node_curr
                    
                    if node_next == end: 
                        reached_end_node = True
                        break
                    
                    self._add_node_to_search_pqueue(node_next)
            if reached_end_node:
                break         
        else:
            return list()  # no path
        
        return self._reconstruct_path(start, end)        
            