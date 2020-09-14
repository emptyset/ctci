"""
4.6
Write an algorithm to find the "next" node (i.e., in-order successor) of a
given node in a binary search tree.  You may assume each node has a link to its
parent.
"""


def get_next(node):
    """
    One implicit bit of information here to pay attention to is that a binary
    search tree is not guaranteed to be balanced.

    Really, this question is two problems.

    The first problem is to determine which of these cases applies:
    - If there is a right child, then the successor is the minimum node in the
      subtree rooted by the right child.
    - If there is no right child, traverse until you reach a parent that is
      greater than or equal to the node, and this is the successor.  If you do
      not find any such parent, there is no successor.
    - If there is no right child, and no parent, then there is no successor.

    The second problem is a left-traversal to find a minimum node in a tree.
    """
    if node is None:
        return None

    if node.right is None:
        # locate the first parent (or not) that exceeds the node's value
        current = node.parent
        while current is not None:
            if current.value >= node.value:
                return current
            current = current.parent
    else:
        # search the subtree for the minimum value
        return get_minimum(node.right)

    # if no successor parent was found, there is no successor
    return None


def get_minimum(node):
    if node is None:
        return None

    minimum = None

    current = node
    while current is not None:
        if minimum is None or minimum.value >= current.value:
            minimum = current

        current = current.left

    return minimum
