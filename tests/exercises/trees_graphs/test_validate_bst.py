from exercises.lib.tree import BinaryNode

from exercises.trees_graphs.minimal_tree import to_bst
from exercises.trees_graphs.validate_bst import is_bst


def test_is_bst__nothing():
    assert is_bst(None)


def test_is_bst__one():
    assert is_bst(BinaryNode(1))


def test_is_bst__simple():
    root = BinaryNode(2, left=BinaryNode(1), right=None)
    assert is_bst(root)


def test_is_bst__complex():
    root = to_bst([1, 2, 3, 4, 5, 6, 7, 8])
    assert is_bst(root)


def test_is_bst__not_at_all():
    root = BinaryNode(7, left=BinaryNode(9), right=BinaryNode(1))
    assert not is_bst(root)
