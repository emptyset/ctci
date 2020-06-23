from exercises.lib.matrix import Position


"""
1.8
Write an algorithm such that if an element in a MxN matrix is 0, its entire row
and column are set to 0.
"""


def zero(m):
    """
    The general idea is to avoid backtracking.  If the problem is approached as
    presented, the time complexity becomes quadratic, as zeros are written back
    over cells already zero'd out.  It's not necessary to do so.

    One algorithm that can run in O(MxN) time is to make a pass over the
    matrix, and then record any zero cell positions in respective row, column
    sets.  In a second pass, test the element's position in both sets, and if
    there is a hit, then write a zero in the cell.

    There is a simple optimization, by running to the end of the row array (in
    the matrix representation we are using) to write zeros, but I'm leaving
    this out because it doesn't materially adjust the complexity.
    """
    zero_rows = set()
    zero_cols = set()

    for r in range(0, m.rows):
        for c in range(0, m.cols):
            if m.get(Position(r, c)) == 0:
                zero_rows.add(r)
                zero_cols.add(c)

    for r in range(0, m.rows):
        for c in range(0, m.cols):
            if r in zero_rows or c in zero_cols:
                m.update(Position(r, c), 0)
