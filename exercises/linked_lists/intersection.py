from collections import defaultdict


"""
2.7
Given two (singly) linked lists, determine if the two lists intersect.  Return
the intersecting node.  Note that intersection is defined based on reference,
not value.  That is, if the kth node of the first linked list is the exact same
node (by reference) as the jth node of the second linked list, then they are
intersecting.
"""


def intersects(left, right):
    """
    The quick solution to this is to use a hash, so that the overall runtime is
    O(N+M).
    """
    visited = defaultdict(lambda: True)
    for element in left:
        visited[element]

    for element in right:
        if element in visited:
            return element

    return None
