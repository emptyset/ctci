from exercises.lib.graph import Graph
from exercises.lib.graph import Node

from exercises.trees_graphs.route_between_nodes import has_route


def test_has_route__to_itself():
    a = Node('A', directed=True)
    graph = Graph([a])

    assert has_route(graph, a, a)


def test_has_route__simple():
    a = Node('A', directed=True)
    b = Node('B', directed=True)
    graph = Graph([a, b])
    graph.link(a, b)

    assert has_route(graph, a, b)


def test_has_route__not_across_islands():
    a = Node('A', directed=True)
    b = Node('B', directed=True)
    graph = Graph([a, b])

    assert not has_route(graph, a, b)


def test_has_route__complex():
    a = Node('A', directed=True)
    b = Node('B', directed=True)
    c = Node('C', directed=True)
    d = Node('D', directed=True)
    e = Node('E', directed=True)
    graph = Graph([a, b, c, d, e])

    graph.link(a, b)
    graph.link(b, c)
    graph.link(b, d)
    graph.link(d, e)

    assert has_route(graph, a, e)


def test_has_route__graph_with_cycle():
    a = Node('A', directed=True)
    b = Node('B', directed=True)
    c = Node('C', directed=True)
    d = Node('D', directed=True)
    e = Node('E', directed=True)
    f = Node('F', directed=True)
    g = Node('G', directed=True)
    h = Node('H', directed=True)
    graph = Graph([a, b, c, d, e, f, g, h])

    graph.link(a, b)
    graph.link(b, c)
    graph.link(b, d)
    graph.link(c, e)
    graph.link(d, e)
    graph.link(e, a)
    graph.link(e, f)
    graph.link(e, g)
    graph.link(f, b)
    graph.link(g, c)
    graph.link(g, h)

    assert has_route(graph, a, h)
