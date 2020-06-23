from exercises.lib.matrix import Matrix
from exercises.lib.matrix import Position
from exercises.strings.zero_matrix import zero


def test_zero__empty():
    empty = Matrix([])
    zero(empty)
    assert empty.rows == 0
    assert empty.cols == 0


def test_zero__single_element():
    single = Matrix([[1]])
    zero(single)
    assert single.get(Position(0, 0)) == 1

    single.update(Position(0, 0), 0)
    zero(single)
    assert single.get(Position(0, 0)) == 0


def test_zero__quad():
    quad = Matrix([
        [1, 1],
        [0, 1]
    ])
    zero(quad)
    assert quad.get(Position(0, 0)) == 0
    assert quad.get(Position(0, 1)) == 1
    assert quad.get(Position(1, 0)) == 0
    assert quad.get(Position(1, 1)) == 0


def test_zero__large():
    large = Matrix([
        [1, 2, 3, 4, 5, 6],
        [0, 2, 3, 0, 5, 6],
        [1, 2, 3, 4, 5, 6]
    ])
    zero(large)
    assert large.get(Position(0, 0)) == 0
    assert large.get(Position(0, 1)) == 2
    assert large.get(Position(0, 2)) == 3
    assert large.get(Position(0, 3)) == 0
    assert large.get(Position(0, 4)) == 5
    assert large.get(Position(0, 5)) == 6
    assert large.get(Position(1, 0)) == 0
    assert large.get(Position(1, 1)) == 0
    assert large.get(Position(1, 2)) == 0
    assert large.get(Position(1, 3)) == 0
    assert large.get(Position(1, 4)) == 0
    assert large.get(Position(1, 5)) == 0
    assert large.get(Position(2, 0)) == 0
    assert large.get(Position(2, 1)) == 2
    assert large.get(Position(2, 2)) == 3
    assert large.get(Position(2, 3)) == 0
    assert large.get(Position(2, 4)) == 5
    assert large.get(Position(2, 5)) == 6
