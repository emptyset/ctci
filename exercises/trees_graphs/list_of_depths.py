from collections import defaultdict

"""
4.3
Given a binary tree, design an algorithm which creates a linked list of all the
nodes at each depth (e.g., if you have a tree with depth D, you'll have D
linked lists.)
"""


def to_linked_lists(root):
    """
    A traversal of tree that is tracking the current depth of the node leads to
    an easy solution, if we can track the linked lists via a hash.

    I have an implementation of LinkedList, but here the simplicity of python's
    basic list type used a linked list is just fine.
    """
    lists = defaultdict(lambda: [])
    _traverse(root, 0, lists)
    return list(lists.values())


def _traverse(node, depth, lists):
    if node is None:
        return

    lists[depth].append(node.value)
    _traverse(node.left, depth + 1, lists)
    _traverse(node.right, depth + 1, lists)
