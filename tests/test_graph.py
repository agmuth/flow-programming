from flowprog.graph import Edge, Graph, Node


def test_init_node():
    node = Node(name="a")
    assert isinstance(node, Node)
    assert node.name == "a"


def test_init_edge():
    node_a = Node(name="a")
    node_b = Node(name="b")
    edge_a_b = Edge(nodes=(node_a, node_b))
    assert isinstance(edge_a_b, Edge)
    assert edge_a_b.nodes[0].name == "a"
    assert edge_a_b.nodes[1].name == "b"


def test_init_graph():
    node_a = Node(name="a")
    node_b = Node(name="b")
    node_c = Node(name="c")
    edge_a_b = Edge(nodes=(node_a, node_b))
    edge_b_c = Edge(nodes=(node_b, node_c))
    edge_list = [edge_a_b, edge_b_c]
    node_list = [node_a, node_b, node_c]
    graph = Graph(edge_list=edge_list)
    assert set(edge_list) == set(graph.edges)
    assert set(node_list) == set(graph.nodes)
