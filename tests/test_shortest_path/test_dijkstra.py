from flowprog.graph_objects import Graph, Node, WeightedEdge
from flowprog.path_finding import DijkstrasAlgorithm

node_a = Node(name="a")
node_b = Node(name="b")
node_c = Node(name="c")
node_d = Node(name="d")
node_e = Node(name="e")


WeightedEdge_a_b = WeightedEdge((node_a, node_b), 4)
WeightedEdge_a_c = WeightedEdge((node_a, node_c), 1)
WeightedEdge_c_b = WeightedEdge((node_c, node_b), 2)
node_b_d = WeightedEdge((node_b, node_d), 1)
node_c_d = WeightedEdge((node_c, node_d), 5)
node_d_e = WeightedEdge((node_d, node_e), 3)


WeightedEdge_list = [
    # (!) ordering here is important
    WeightedEdge_a_b,
    WeightedEdge_a_c,
    WeightedEdge_c_b,
    node_b_d,
    node_c_d,
    node_d_e,
]

graph = Graph(WeightedEdge_list)


def test_dijkstra():
    dijkstra = DijkstrasAlgorithm()
    dijkstra_path_found = dijkstra(graph, node_a, node_e)
    dijkstra_path_correct = [node_a, node_c, node_b, node_d, node_e]
    assert dijkstra_path_found == dijkstra_path_correct


if __name__ == "__main__":
    test_dijkstra()
