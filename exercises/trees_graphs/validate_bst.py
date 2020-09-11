"""
4.5
Implement a function to check if a binary tree is a binary search tree.
"""


def is_bst(root):
    """
    The general approach is to recursively assert the binary tree is a binary
    search tree (left node is less than node is less than right node.)
    """
    if root is None:
        return True

    def is_subtree_valid(child, parent, compare):
        if child is not None:
            return compare(child.value, parent.value) and is_bst(child)
        return True

    valid = is_subtree_valid(root.left, root, lambda c, p: c <= p)
    valid &= is_subtree_valid(root.right, root, lambda c, p: c >= p)

    return valid
