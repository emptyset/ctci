from exercises.trees_graphs.build_order import build_order

from pytest import raises


def test_build_order__nothing():
    with raises(Exception):
        _ = build_order(None)

    with raises(Exception):
        _ = build_order([])


def test_build_order__simple_linear():
    deps = [(1, 2), (2, 3), (3, 4), (4, 5)]
    order = build_order(deps)
    assert len(order) == 5
    assert order == [1, 2, 3, 4, 5]


def test_build_order__simple_branch():
    deps = [(1, 2), (2, 3), (3, 4), (3, 5)]
    order = build_order(deps)
    assert len(order) == 5
    assert order == [1, 2, 3, 4, 5] or order == [1, 2, 3, 5, 4]


def test_build_order__complex_branch():
    deps = [(1, 4), (2, 5), (3, 6), (4, 6), (5, 6)]
    order = build_order(deps)
    assert len(order) == 6
    assert set(order[:3]) == set([1, 2, 3])
    assert set(order[3:5]) == set([4, 5])
    assert set(order[5:]) == set([6])


def test_build_order__with_cycle():
    deps = [(1, 2), (2, 3), (3, 4), (4, 1)]
    with raises(Exception):
        _ = build_order(deps)
