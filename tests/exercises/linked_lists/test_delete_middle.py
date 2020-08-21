from exercises.lib.linked_list import LinkedList

from exercises.linked_lists.delete_middle import delete


def test_delete__next_to_head():
    s = set([1, 2, 3, 4, 5])
    ll = LinkedList(s)
    element = ll[1]
    delete(ll, element)
    assert set(ll.values) == set([1, 3, 4, 5])


def test_delete__next_to_tail():
    s = set([1, 2, 3, 4, 5])
    ll = LinkedList(s)
    element = ll[3]
    delete(ll, element)
    assert set(ll.values) == set([1, 2, 3, 5])


def test_delete__middle():
    s = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ll = LinkedList(s)
    element = ll[6]
    delete(ll, element)
    assert set(ll.values) == set([1, 2, 3, 4, 5, 6, 8, 9, 10])
