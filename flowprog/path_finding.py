from collections import defaultdict, deque
from typing import Any, Iterable, List

import numpy as np

from flowprog.graph_objects import Edge, Graph, Node, NodePath


class BreadthFirstSearch:
    def __init__(self) -> None:
        self.search_deque = deque()
        self.visited_nodes = defaultdict(lambda: False)
        self.prev_node_mapping = defaultdict(None)
    
    # static methods included so that max-flow dfs can inherit and override when arcs are at capacity
    
    @staticmethod
    def _edge_cond(edge: Edge) -> bool:
        return True
    
    @staticmethod
    def _edge_constructor(from_node: Node, to_node: Node) -> Edge:
        return Edge((from_node, to_node))

    def _add_edge_to_search_deque(self, edge: Edge) -> None:
        self.search_deque.append(edge)

    def _get_edge_from_search_deque(self) -> Edge:
        # FIFO
        return self.search_deque.popleft()

    def _reconstruct_node_path(self, start: Node, end: Node) -> NodePath:
        if end not in self.prev_node_mapping.keys(): return list()
        
        path = [end]
        while path[-1] != start:
            path.append(self.prev_node_mapping[path[-1]])
        return path[::-1]

    def __call__(self, graph: Graph, start: Node, end: Node) -> NodePath:
        self.__init__() # need to re init for multiple calls
        self._add_edge_to_search_deque(self._edge_constructor(None, start))

        while len(self.search_deque) > 0:
            edge_to_search_along = self._get_edge_from_search_deque()
            
            if not self._edge_cond(edge_to_search_along):
                continue
            
            prev_node, curr_node = edge_to_search_along.nodes

            if self.visited_nodes[curr_node]:
                continue

            self.visited_nodes[curr_node] = True
            self.prev_node_mapping[curr_node] = prev_node

            if curr_node == end:
                break

            for edge in graph.edge_list[curr_node]:
                self._add_edge_to_search_deque(edge)

        return self._reconstruct_node_path(start, end)


class DepthFirstSearch(BreadthFirstSearch):
    def _get_edge_from_search_deque(self) -> Edge:
        # LIFO
        return self.search_deque.pop()

