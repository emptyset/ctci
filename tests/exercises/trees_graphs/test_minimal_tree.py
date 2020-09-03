from math import floor
from math import log2

from exercises.trees_graphs.minimal_tree import to_bst


def maximum_height(n):
    return floor(log2(n)) + 1


def test_to_bst__nothing():
    assert to_bst([]) is None


def test_to_bst__one():
    array = [1]
    assert to_bst(array).traverse_inorder() == array


def test_to_bst__many_even():
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    root = to_bst(array)
    assert root.traverse_inorder() == array
    assert root.height <= maximum_height(len(array))


def test_to_bst__many_odd():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    root = to_bst(array)
    assert root.traverse_inorder() == array
    assert root.height <= maximum_height(len(array))
