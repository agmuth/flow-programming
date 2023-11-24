from collections import defaultdict
from typing import Any, Tuple

import numpy as np

from flowprog.graph_objects import Graph, Node
from flowprog.path_finding import BreadthFirstSearch


class DijkstrasAlgorithm(BreadthFirstSearch):
    def __init__(self) -> None:
        super().__init__()
        self.node_dist = defaultdict(lambda: np.Inf)

    def _add_node_to_search_deque(self, node: Node) -> None:
        dist = self.node_dist[node]
        for i, elem in enumerate(self.search_deque):
            if elem[0] < dist:
                self.search_deque.insert(i + 1, (dist, node))
                break
        else:
            self.search_deque.append((dist, node))

    def _get_node_from_search_deque(self) -> Tuple[float, Node]:
        return self.search_deque.pop()[1]

    def __call__(self, graph: Graph, start: Node, end: Node) -> Any:
        reached_end_node = False
        self.node_dist[start] = 0
        self._add_node_to_search_deque(start)

        while len(self.search_deque) > 0:
            node_curr = self._get_node_from_search_deque()
            dist_curr = self.node_dist[node_curr]

            if self.visited_nodes[node_curr]:
                continue

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

                    self._add_node_to_search_deque(node_next)
            self.visited_nodes[node_curr] = True
            if reached_end_node:
                break

        else:
            return list()  # no path

        return self._reconstruct_path(start, end)
