from exercises.lib.linked_list import LinkedList

from exercises.linked_lists.partition import partition


def validate(ll, partition):
    valid = True
    check_left = True
    for value in ll.values:
        if value >= partition:
            check_left = False

        if check_left:
            valid &= value < partition
        else:
            valid &= value >= partition

    return valid


def test_partition__example():
    ll = partition(LinkedList([3, 5, 8, 5, 10, 2, 1]), 5)
    assert validate(ll, 5)


def test_partition__no_left_side():
    ll = partition(LinkedList([5, 6, 7, 8, 9, 10]), 4)
    assert validate(ll, 4)


def test_partition__no_right_side():
    ll = partition(LinkedList([1, 2, 3, 4, 5, 6]), 7)
    assert validate(ll, 7)


def test_partition__one():
    ll = partition(LinkedList([1]), 1)
    assert validate(ll, 1)


def test_partition__none():
    ll = partition(LinkedList([]), 0)
    assert len(ll) == 0
