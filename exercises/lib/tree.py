class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self._value = value
        self.left = left
        self.right = right

    @property
    def value(self):
        return self._value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node

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
