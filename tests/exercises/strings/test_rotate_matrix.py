from exercises.lib.matrix import Matrix
from exercises.strings.rotate_matrix import rotate_matrix


def make_matrix(row_strings):
    m = []
    for s in row_strings:
        m.append(list(s))
    return Matrix(m)


def validate(actual, expected):
    for actual_row, expected_row in zip(actual.m, expected.m):
        assert actual_row == expected_row


def test_rotate_matrix__empty():
    empty = make_matrix([])
    validate(rotate_matrix(empty), empty)


def test_rotate_matrix__simple():
    simple = make_matrix(['Z'])
    validate(rotate_matrix(simple), simple)


def test_rotate_matrix__odd():
    rows = [
        'abc',
        'hZd',
        'gfe'
    ]
    odd = make_matrix(rows)

    rows = [
        'gha',
        'fZb',
        'edc'
    ]
    expected = make_matrix(rows)

    validate(rotate_matrix(odd), expected)


def test_rotate_matrix__even():
    rows = [
        'abcd',
        'lWXe',
        'kZYf',
        'jihg'
    ]
    even = make_matrix(rows)

    rows = [
        'jkla',
        'iZWb',
        'hYXc',
        'gfed'
    ]
    expected = make_matrix(rows)

    validate(rotate_matrix(even), expected)
