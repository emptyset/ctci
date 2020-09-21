"""
4.8
Design an algorithm and write code to find the first common ancestor of two
nodes in a binary tree.  Avoid storing additional nodes in a data structure.
NOTE: This is not necessarily a binary search tree.
"""


def find(left, right):
    """
    Without the restriction on data structure, this problem is identical to the
    linked list intersection problem, except modifying the iterator to return
    the parent node on the next invocation.

    As in that solution, I'd use a hash and iterate up to the root on one
    branch, and then test membership on each iteration step on the other
    branch.  Runtime of O(log n).

    If we could assume a binary search tree, then the common ancestor is the
    "left" child of the first parent node whose value exceeds the "right"
    node's value.  Also a runtime of O(log n).

    Since the nodes can't be cached in a data structure to facilitate lookup,
    we trade the space savings for a runtime penalty.

    The algorithm works by iterating up the "left"* node up to the root, and
    testing if there is a match to the current "right"* node.  If no match,
    then move the current "right" node up to its parent and test membership on
    iterating over the "left" branch again.  The runtime here is O(log^2 n).

    * In this function, "left" and "right" does not strictly imply that the
    nodes are to the left or right of each other in terms of their first common
    ancestor node.
    """
    current = right
    while current is not None:
        branch_node = left
        while branch_node is not None:
            if branch_node == current:
                return current
            branch_node = branch_node.parent
        current = current.parent

    return None
