from collections import defaultdict, deque
from typing import Any, Iterable

from flowprog.graph import Edge, Graph, Node


class BreadthFirstSearch:
    def __init__(self) -> None:
        self.search_deque = deque()
        self.visited_nodes = defaultdict(lambda: False)
        self.curr_prev_node_mapping = defaultdict(None)

    def _add_edge_to_search_deque(self, edge: Edge) -> None:
        self.search_deque.append(edge)

    def _get_edge_from_search_deque(self) -> Edge:
        # FIFO
        return self.search_deque.popleft()

    def _reconstruct_path(self, start: Node, end: Node) -> Iterable[Node]:
        path = [end]
        while path[-1] != start:
            path.append(self.curr_prev_node_mapping[path[-1]])
        return path[::-1]

    def __call__(self, graph: Graph, start: Node, end: Node) -> Any:
        self._add_edge_to_search_deque(Edge((None, start)))

        while len(self.search_deque) > 0:
            edge_to_search_along = self._get_edge_from_search_deque()
            prev_node, curr_node = edge_to_search_along.nodes

            if self.visited_nodes[curr_node]:
                continue

            self.visited_nodes[curr_node] = True
            self.curr_prev_node_mapping[curr_node] = prev_node

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
