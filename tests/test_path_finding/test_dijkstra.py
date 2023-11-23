from flowprog.graph import Edge, Graph, Node
from flowprog.path_finding import DijkstrasAlgorithm

node_a = Node(name="a")
node_b = Node(name="b")
node_c = Node(name="c")
node_d = Node(name="d")
node_e = Node(name="e")


edge_a_b = Edge((node_a, node_b), 4)
edge_a_c = Edge((node_a, node_c), 1)
edge_c_b = Edge((node_c, node_b), 2)
node_b_d = Edge((node_b, node_d), 1)
node_c_d = Edge((node_c, node_d), 5)
node_d_e = Edge((node_d, node_e), 3)


edge_list = [
    # (!) ordering here is important
    edge_a_b,
    edge_a_c,
    edge_c_b,
    node_b_d,
    node_c_d,
    node_d_e,
]

graph = Graph(edge_list)


def test_dijkstra():
    dijkstra = DijkstrasAlgorithm()
    dijkstra_path_found = dijkstra(graph, node_a, node_e)
    dijkstra_path_correct = [node_a, node_c, node_b, node_d, node_e]
    assert dijkstra_path_found == dijkstra_path_correct


if __name__ == "__main__":
    test_dijkstra()