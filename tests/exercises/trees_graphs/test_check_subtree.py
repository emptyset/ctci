from exercises.lib.tree import BinaryNode

from exercises.trees_graphs.check_subtree import check


def test_check__none_is_subtree():
    assert check(BinaryNode(1), None)


def test_check__none_cannot_have_subtrees():
    assert not check(None, BinaryNode(1))


def test_check__single_node_subtree():
    tree = BinaryNode(2, left=BinaryNode(1), right=BinaryNode(3))
    assert check(tree, BinaryNode(1))
    assert check(tree, BinaryNode(3))


def test_check__against_self():
    tree = BinaryNode(2, left=BinaryNode(1), right=BinaryNode(3))
    assert check(tree, tree)


def test_check__complex_subtree():
    tree = BinaryNode(5)
    tree.left = BinaryNode(3)
    tree.right = BinaryNode(7)
    tree.left.left = BinaryNode(2)
    tree.left.right = BinaryNode(4)
    tree.right.left = BinaryNode(6)
    tree.right.right = BinaryNode(8)

    assert check(tree, BinaryNode(7, left=BinaryNode(6), right=BinaryNode(8)))
