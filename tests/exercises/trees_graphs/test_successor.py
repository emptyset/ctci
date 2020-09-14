from exercises.lib.tree import BinaryNode

from exercises.trees_graphs.successor import get_next


def test_get_next__nothing():
    assert get_next(None) is None


def test_get_next__no_successor_self_is_at_root():
    assert get_next(BinaryNode(1)) is None


def test_get_next__simple_successor():
    node = BinaryNode(1, right=BinaryNode(2))
    assert get_next(node).value == 2


def test_get_next__parent_is_successor():
    node = BinaryNode(2, left=BinaryNode(1))
    assert get_next(node.left).value == 2


def test_get_next__successor_complex():
    A = BinaryNode(1)
    C = BinaryNode(3)
    B = BinaryNode(2, left=A, right=C)
    D = BinaryNode(4, left=B, right=None)
    assert get_next(A).value == 2
    assert get_next(B).value == 3
    assert get_next(C).value == 4
    assert get_next(D) is None
