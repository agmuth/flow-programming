from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from functools import reduce
from typing import Any, Iterable, List, Optional, Tuple


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

    @property
    def nodes(self) -> List[Node]:
        return list(self.node_list.keys())

    @property
    def edges(self) -> List[Edge]:
        return reduce(lambda l1, l2: l1 + l2, self.edge_list.values())
