from exercises.trees_graphs.list_of_depths import to_linked_lists
from exercises.trees_graphs.minimal_tree import to_bst


def test_to_linked_lists__nothing():
    lists = to_linked_lists(None)
    assert len(lists) == 0


def test_to_linked_lists__one():
    lists = to_linked_lists(to_bst([9000]))
    assert len(lists) == 1
    assert len(lists[0]) == 1
    assert lists[0][0] == 9000


def test_to_linked_lists__many():
    lists = to_linked_lists(to_bst([1, 2, 3, 4, 5, 6, 7, 8]))
    assert len(lists) == 4

    assert [1, 1, 2, 4] == sorted([len(li) for li in lists])
