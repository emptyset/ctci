from exercises.lib.matrix import Position


"""
1.7
Given an image represented by a NxN matrix, where each pixel in the image is
4 bytes, write a method to rotate the image by 90 degrees.  Can you do this
in place?
"""


def rotate_matrix(m):
    """
    I visualize the in-place rotation as (no pun intended) a string
    wrapped around a block, representing the values of the matrix in the
    outer columns and rows.  In order to rotate in-place, the string is just
    moved around the block - so for example, if the string were tied back onto
    itself with a knot on the upper left corner, rotating the string clockwise
    would put the knot in the upper right corner of the matrix.  Or more
    concretely:

        W - - - X         Z o o o W
        o . . . o         - . . . -
        o . . . o   -->   - . . . -
        o . . . o         - . . . -
        Z - - - Y         Y o o o X

    The process can be repeated down to the center of the matrix, where we
    either end up with a 2x2 submatrix if N is even, and a single pixel if
    N is odd.  Recursion can be used if the index bounds for submatrices are
    carefully provided at each step.

    The time complexity of the algorithm is linear relative to the number of
    elements in the matrix, O(n) where n = NxN.

    The space complexity can be constant if a 16-byte (4 x 4-byte) buffer is
    used to "walk" around the edge of the matrix or submatrix, writing values
    as they appear, instead of capturing the entire edge as a string, and then
    shifting it.

    It became a lot easier in a subsequent pass of the code to setup some
    helper classes to represent the bounds of the current matrix "border
    string" and the current rotation buffer.
    """
    return _rotate(m, _get_new_bounds(m))


class Bounds:
    @classmethod
    def from_matrix(cls, m):
        if m.rows <= 1:
            return None

        return cls(top=0, right=m.cols - 1, bottom=m.rows - 1, left=0)

    def __init__(self, top=None, right=None, bottom=None, left=None):
        self._top = top
        self._right = right
        self._bottom = bottom
        self._left = left

    @property
    def top(self):
        return self._top

    @property
    def right(self):
        return self._right

    @property
    def bottom(self):
        return self._bottom

    @property
    def left(self):
        return self._left

    def decrement(self):
        self._top = self.top + 1
        self._right = self.right - 1
        self._bottom = self.bottom - 1
        self._left = self.left + 1

    def are_valid(self):
        return self.top < self.bottom and self.left < self.right


class RotationBuffer:
    def __init__(self, bounds):
        self._positions = []
        self.positions.append(Position(bounds.top, bounds.left))
        self.positions.append(Position(bounds.top, bounds.right))
        self.positions.append(Position(bounds.bottom, bounds.right))
        self.positions.append(Position(bounds.bottom, bounds.left))

    @property
    def positions(self):
        return self._positions

    def apply(self, m):
        values = [m.get(position) for position in self.positions]
        last = values.pop()
        values.insert(0, last)

        for position, value in zip(self.positions, values):
            m.update(position, value)

    def step(self):
        self.positions[0].col = self.positions[0].col + 1
        self.positions[1].row = self.positions[1].row + 1
        self.positions[2].col = self.positions[2].col - 1
        self.positions[3].row = self.positions[3].row - 1


def _get_new_bounds(m, bounds=None):
    if bounds is None:
        return Bounds.from_matrix(m)

    bounds.decrement()

    if bounds.are_valid():
        return bounds

    return None


def _rotate(m, bounds=None):
    if bounds is None:
        return m

    rotation_buffer = RotationBuffer(bounds)

    for index in range(bounds.left, bounds.right):
        rotation_buffer.apply(m)
        rotation_buffer.step()

    return _rotate(m, _get_new_bounds(m, bounds))
