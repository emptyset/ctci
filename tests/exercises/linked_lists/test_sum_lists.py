from exercises.lib.linked_list import LinkedList

from exercises.linked_lists.sum_lists import sum


def test_sum__reverse_nothing():
    left = LinkedList([])
    right = LinkedList([])
    assert list(sum(left, right).values) == []


def test_sum__reverse_zero():
    left = LinkedList([0])
    right = LinkedList([0])
    assert list(sum(left, right).values) == [0]


def test_sum__reverse_example():
    left = LinkedList([7, 1, 6])
    right = LinkedList([5, 9, 2])
    assert list(sum(left, right).values) == [2, 1, 9]


def test_sum__reverse_plus_carry():
    left = LinkedList([9, 1, 6])
    right = LinkedList([5, 9, 9])
    assert list(sum(left, right).values) == [4, 1, 6, 1]


def test_sum__not_reversed_nothing():
    left = LinkedList([])
    right = LinkedList([])
    assert list(sum(left, right, reverse=False).values) == []


def test_sum__not_reversed_zero():
    left = LinkedList([0])
    right = LinkedList([0])
    assert list(sum(left, right, reverse=False).values) == [0]


def test_sum__not_reversed_example():
    left = LinkedList([6, 1, 7])
    right = LinkedList([2, 9, 5])
    assert list(sum(left, right, reverse=False).values) == [9, 1, 2]


def test_sum__not_reversed_plus_carry():
    left = LinkedList([6, 1, 9])
    right = LinkedList([9, 9, 5])
    assert list(sum(left, right, reverse=False).values) == [1, 6, 1, 4]
