from collections import defaultdict


"""
2.8
Given a circular linked list, implement an algorithm that returns the node at
the beginning of the loop.
"""


def has_loop(ll):
    """
    Similar to identifying intersections, using a hash for the references is
    the method to detect a loop in a singly linked list.
    """
    visited = defaultdict(lambda: True)
    for element in ll:
        if element in visited:
            return element
        else:
            visited[element]

    return None
