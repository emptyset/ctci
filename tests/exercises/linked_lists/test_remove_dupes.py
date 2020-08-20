from exercises.lib.linked_list import LinkedList

from exercises.linked_lists.remove_dupes import remove_dupes__using_set
from exercises.linked_lists.remove_dupes import remove_dupes__no_buffer


def test_remove_dupes__no_dupes():
    s = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ll = LinkedList(s)
    assert set(remove_dupes__using_set(ll)) == s
    assert set(remove_dupes__no_buffer(ll)) == s


def test_remove_dupes__with_dupes():
    s = set([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    ll = LinkedList(s)

    s_no_dupes = set([1, 2, 3, 4, 5])
    assert set(remove_dupes__using_set(ll)) == s_no_dupes
    assert set(remove_dupes__no_buffer(ll)) == s_no_dupes
