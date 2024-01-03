from collections import defaultdict
from typing import List, Tuple, Union

import numpy as np

from flowprog.graph_objects import Graph, Node, NodePath
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

    def __call__(self, graph: Graph, start: Node, end: Node) -> NodePath:
        self.__init__()  # need to re init for multiple calls
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

        return self._reconstruct_node_path(start, end)


class FloydWarshallAlgorithm:
    def __init__(self) -> None:
        self.node_dist_mapping = defaultdict(lambda: defaultdict(lambda: np.inf))
        self.prev_node_mapping = defaultdict(None)

    def dist(self, start: Node, end: Node) -> float:
        return self.node_dist_mapping[start][end]

    def path(self, start: Node, end: Node) -> NodePath:
        if self.node_dist_mapping[start][end] is None:
            return list()  # no path
        path = [end]
        while path[-1] != start:
            path.append(self.prev_node_mapping[path[-1]])
        return path[::-1]

    def get_negative_cycles(self) -> Union[None, List[NodePath]]:
        pass

    def __call__(self, graph: Graph) -> None:
        self.__init__()  # need to re init for multiple calls

        # init dist and prev mappings
        for node in graph.nodes:
            self.node_dist_mapping[node][node] = 0
            self.prev_node_mapping[node] = node

        for edge in graph.edges:
            from_node, to_node = edge.nodes
            self.node_dist_mapping[from_node][to_node] = edge.weight
            self.prev_node_mapping[to_node] = from_node

        # main body of algo
        for node_k in graph.nodes:
            for node_i in graph.nodes:
                for node_j in graph.nodes:
                    if (
                        self.node_dist_mapping[node_i][node_j]
                        > self.node_dist_mapping[node_i][node_k]
                        + self.node_dist_mapping[node_k][node_j]
                    ):
                        self.node_dist_mapping[node_i][node_j] = (
                            self.node_dist_mapping[node_i][node_k]
                            + self.node_dist_mapping[node_k][node_j]
                        )
                        self.prev_node_mapping[node_j] = node_k
