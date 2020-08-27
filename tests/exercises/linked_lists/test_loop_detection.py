from exercises.lib.linked_list import LinkedList

from exercises.linked_lists.loop_detection import has_loop


def test_has_loop__yes():
    ll = LinkedList([1, 2, 3, 4, 5])
    element = ll[4]
    element.next = ll[1]

    assert has_loop(ll) == ll[1]
    assert ll[5] == ll[1]


def test_has_loop__no():
    ll = LinkedList([1, 2, 3, 4, 5])

    assert has_loop(ll) is None
