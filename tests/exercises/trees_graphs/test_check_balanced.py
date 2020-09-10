from exercises.lib.tree import BinaryNode

from exercises.trees_graphs.check_balanced import is_balanced


def test_is_balanced__nothing():
    assert is_balanced(None)


def test_is_balanced__one():
    assert is_balanced(BinaryNode(1))


def test_is_balanced__simple():
    assert is_balanced(BinaryNode(2, left=BinaryNode(1), right=BinaryNode(3)))


def test_is_balanced__complex_in_balance():
    root = BinaryNode(5)
    root.left = BinaryNode(3)
    root.right = BinaryNode(7)
    root.left.left = BinaryNode(2)
    root.left.right = BinaryNode(4)
    root.right.left = BinaryNode(6)
    root.right.right = BinaryNode(8)
    assert is_balanced(root)


def test_is_balanced__complex_left_is_smaller():
    root = BinaryNode(5)
    root.left = BinaryNode(3)
    root.right = BinaryNode(7)
    root.right.left = BinaryNode(6)
    root.right.right = BinaryNode(8)
    assert is_balanced(root)


def test_is_balanced__complex_right_is_smaller():
    root = BinaryNode(5)
    root.left = BinaryNode(3)
    root.right = BinaryNode(7)
    root.left.left = BinaryNode(2)
    root.left.right = BinaryNode(4)
    assert is_balanced(root)
