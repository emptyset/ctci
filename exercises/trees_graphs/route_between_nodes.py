from collections import deque


"""
4.1
Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
"""


def has_route(graph, origin, target):
    """
    The instructions don't specify runtime restrictions, nor do they specify
    that the route has to be returned, only to indicate that a route exists.

    A depth-first traversal of a graph is less efficient, but it is generally
    easier to return a full route this way.

    One issue to address in a graph algorithm is avoiding cycles.  These
    instructions don't indicate that the graph is acyclic, so it's best to
    maintain a set of visited nodes.

    Another issue is whether the graph nodes are connected; it's possible for a
    graph to consist of several, unconnected subgraphs in the most general
    definition.  This algorithm doesn't explicitly account for this, because it
    turns out if the target node is in a separate, disconnected subgraph, then
    there is no route when we start from origin.

    For strictly asserting whether or not a route exists, I'm more inclined to
    use a breadth-first traversal (via a queue) until the target node is
    located, or the entire queue is empty.  Only unvisited nodes are added to
    the queue.

    To facilitate this, I'll create a Graph and Node class in the library.
    """
    if target in origin.outgoing:
        return True

    queue = deque([origin])
    visited = {}

    while len(queue) > 0:
        current = queue.popleft()
        visited[current] = True

        if current == target:
            return True

        for node in current.outgoing:
            if node not in visited:
                queue.append(node)

    return False
