class BinaryNode:
    def __init__(self, value, left=None, right=None, parent=None):
        self._value = value
        self.left = left
        self.right = right
        self.parent = parent

    @property
    def value(self):
        return self._value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node
        if self._left is not None:
            self._left.parent = self

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
        if self._right is not None:
            self._right.parent = self

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        self._parent = node

    @property
    def height(self):
        left_height = 0
        if self.left is not None:
            left_height += self.left.height

        right_height = 0
        if self.right is not None:
            right_height += self.right.height

        return max(left_height, right_height) + 1

    def traverse_inorder(self):
        output = []

        if self.left is not None:
            output += self.left.traverse_inorder()

        output.append(self.value)

        if self.right is not None:
            output += self.right.traverse_inorder()

        return output
