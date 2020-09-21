from exercises.lib.tree import BinaryNode

from exercises.trees_graphs.first_common_ancestor import find


def test_find__nothing():
    assert find(None, None) is None


def test_find__only_the_root():
    root = BinaryNode(1)
    assert find(root, root) == root


def test_find__it_is_the_root():
    left = BinaryNode(1)
    right = BinaryNode(9)
    root = BinaryNode(5, left=left, right=right)
    assert find(left, right) == root


def test_find__something_in_the_middle():
    root = BinaryNode(5)
    root.left = BinaryNode(3)
    root.right = BinaryNode(7)
    root.left.left = BinaryNode(2)
    root.left.right = BinaryNode(4)
    root.right.left = BinaryNode(6)
    root.right.right = BinaryNode(8)
    assert find(root.left.left, root.left.right) == root.left
