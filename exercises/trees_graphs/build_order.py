from collections import deque

from exercises.lib.graph import Graph
from exercises.lib.graph import Node


"""
4.7
You are given a list of projects and a list of dependencies (which is a list of
pairs of projects, where the second project is dependent on the first project.)
All of a project's dependencies must be built before the project is.  Find a
build order that will allow the projects to be built.  If there is no valid
build order, return an error.
"""


def build_order(pairs):
    """
    The general idea is to build a directed graph from the dependencies, and
    then traverse the graph's nodes from the "root" nodes, nodes that have zero
    incoming nodes.

    There is two situations where a graph doesn't have a valid build order.
    The first is if a cycle is present.  The second is a subcase of the first,
    in which there are no nodes with zero incoming nodes.

    This problem was more involved than expected, as there are a number of
    pitfalls when carefully trying to determine the order and what has already
    been built.
    """
    graph = Graph()
    for pair in pairs:
        if len(pair) != 2:
            raise ValueError

        source = get_node(pair[0], graph)
        target = get_node(pair[1], graph)

        graph.link(source, target)

    roots = get_roots(graph)
    if len(roots) == 0:
        raise ValueError

    order = []
    built = set()
    queue = deque(roots)

    while len(queue) > 0:
        node = queue.popleft()

        if node in built:
            # cycle detected
            raise ValueError

        # breaks Node encapsulation :(
        if node.incoming.issubset(built):
            built.add(node)
            # don't add in any dependency already in the queue
            queue.extend(node.outgoing - set(queue))

            order.append(node.value)
        else:
            # add it back to the end
            queue.append(node)

    return order


def get_node(value, graph):
    for node in graph.nodes:
        if node.value == value:
            return node

    node = Node(value, directed=True)
    graph.nodes.add(node)

    return node


def get_roots(graph):
    return list(filter(lambda node: len(node.incoming) == 0, graph.nodes))
