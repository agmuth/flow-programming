from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from functools import reduce
from typing import Any, Iterable, List, NewType, Optional, Tuple


@dataclass
class Node:
    name: Any

    def __str__(self):
        attrs = [self.name]
        return "".join([str(x) for x in attrs])

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other: Node):
        return hash(self) == hash(other)


@dataclass
class Edge:
    nodes: Tuple[Node, Node]

    def __str__(self):
        attrs = [*self.nodes]
        return "".join([str(x) for x in attrs])

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other: Edge):
        return hash(self) == hash(other)


@dataclass
class WeightedEdge(Edge):
    weight: float = 0.0


@dataclass
class CapacitatedEdge(Edge):
    capacity: float = 0.0
    flow: float = 0

    @property
    def is_residual(self):
        return self.capacity == 0.0

    @property
    def remaining_capacity(self):
        return self.capacity - self.flow

    def augment_flow(self, augmenting_flow: float):
        self.flow += augmenting_flow * (-1 if self.is_residual else 1)


@dataclass
class CapacitatedCostEdge(Edge):
    cost: float = 0.0
    capacity: float = 0.0
    flow: float = 0.0
    is_back_edge: bool = False

    @property
    def weight(self):
        return self.cost

    @property
    def remaining_capacity(self):
        return self.capacity - self.flow

    def augment_flow(self, augmenting_flow: float):
        self.flow += augmenting_flow

    @property
    def is_residual(self):
        return False


NodePath = NewType("NodePath", List[Node])
EdgePath = NewType("EdgePath", List[Edge])

# @dataclass
# class NodePath:
#     path: List[Node]


# @dataclass
# class EdgePath:
#     path: List[Edge]


class Graph:
    def __init__(self, edge_list: Optional[Iterable[Edge]] = None) -> None:
        self.edge_list = defaultdict(list)
        self.node_list = defaultdict(None)
        if edge_list:
            for edge in edge_list:
                self.add_edge(edge)

    def add_edge(self, edge: Edge) -> None:
        self.node_list[edge.nodes[0]] = None
        self.node_list[edge.nodes[1]] = None
        self.edge_list[edge.nodes[0].name].append(edge)

    def remove_edge(self, edge: Edge) -> None:
        self.edge_list[edge.nodes[0]].remove(edge)

    def get_edge(self, node_from: Node, node_to: Node) -> Edge:
        for edge in self.edge_list[node_from]:
            if edge.nodes[1] == node_to:
                return edge

    @property
    def nodes(self) -> List[Node]:
        return list(self.node_list.keys())

    @property
    def edges(self) -> List[Edge]:
        return reduce(lambda l1, l2: l1 + l2, self.edge_list.values())

    def get_edge_path(self, node_path: NodePath):
        return EdgePath(
            [
                self.get_edge(node_from, node_to)
                for node_from, node_to in zip(node_path[:-1], node_path[1:])
            ]
        )
