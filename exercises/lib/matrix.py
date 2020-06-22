class Matrix:
    def __init__(self, m):
        self._m = m

    @property
    def m(self):
        return self._m

    @property
    def rows(self):
        return len(self._m)

    @property
    def cols(self):
        if self.rows > 0:
            return len(self._m[0])
        else:
            return 0

    def get(self, position):
        return self._m[position.row][position.col]

    def update(self, position, value):
        self._m[position.row][position.col] = value


class Position:
    def __init__(self, row, col):
        self._row = row
        self._col = col

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, value):
        self._row = value

    @property
    def col(self):
        return self._col

    @col.setter
    def col(self, value):
        self._col = value
