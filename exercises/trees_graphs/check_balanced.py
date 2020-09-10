"""
4.4
Implement a function to check if a binary tree is balanced.  For the purposes
of this question, a balanced tree is defined to be a tree such that the heights
of the two subtrees of any node never differ by more than one.
"""


def is_balanced(root):
    """
    This is a traversal problem again.

    The height property already performs the traversal, but we'll have to guard
    against None values for the root's left and right nodes.
    """
    if root is None:
        return True

    left_height = _get_height(root.left)
    right_height = _get_height(root.right)

    min_ok = right_height - 1 <= left_height <= right_height
    max_ok = right_height <= left_height <= right_height + 1

    return min_ok or max_ok


def _get_height(node):
    if node is None:
        return 0

    return node.height
