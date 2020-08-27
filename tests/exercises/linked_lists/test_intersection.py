from exercises.lib.linked_list import LinkedList

from exercises.linked_lists.intersection import intersects


def test_intersects__yes():
    left = LinkedList([1, 2, 3, 4, 5])
    element = left[3]

    right = LinkedList([1, 2])
    right.append(element)

    assert intersects(left, right) == element


def test_intersects__no():
    left = LinkedList([1, 2, 3, 4, 5])
    right = LinkedList([1, 2, 3, 4, 5])

    assert intersects(left, right) is None
