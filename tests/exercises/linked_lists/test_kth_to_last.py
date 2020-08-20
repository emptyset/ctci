from exercises.lib.linked_list import LinkedList

from exercises.linked_lists.kth_to_last import get_kth_to_last


def test_get_kth_to_last__well_out_of_bounds():
    ll = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    k = 16
    assert get_kth_to_last(k, ll) is None


def test_get_kth_to_last__out_of_bounds():
    ll = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    k = 10
    assert get_kth_to_last(k, ll) is None


def test_get_kth_to_last__almost_out_of_bounds():
    ll = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    k = 9
    assert get_kth_to_last(k, ll) == 1


def test_get_kth_to_last__well_in_bounds():
    ll = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    k = 2
    assert get_kth_to_last(k, ll) == 8


def test_get_kth_to_last__multiple_of_two():
    ll = LinkedList([1, 2, 3, 4, 5, 6, 7, 8])
    k = 2
    assert get_kth_to_last(k, ll) == 6


def test_get_kth_to_last__way_back():
    ll = LinkedList([1, 2, 3, 4, 5, 6, 7, 8])
    k = 7
    assert get_kth_to_last(k, ll) == 1
