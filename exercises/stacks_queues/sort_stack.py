"""
3.5
Write a program to sort a stack such that the smallest items are on the top.
You can use an additional temporary stack, but you may not copy the elements
into any other data structure (such as an array.)
"""


class Stack:
    """
    Quick implementation of a stack to facilitate parameters of the question.
    """
    def __init__(self):
        self._s = []

    def push(self, item):
        self._s.append(item)

    def pop(self):
        if len(self._s) > 0:
            return self._s.pop()
        return None

    def peek(self):
        if len(self._s) > 0:
            return self._s[len(self._s) - 1]
        return None

    @property
    def empty(self):
        return len(self._s) == 0


def sort_stack(stack):
    """
    The strategy here is to basically do insertion sort on the temporary stack
    such that the largest elements are on top, and then the elements can be
    added back to the original stack so that the smallest elements are on top.

    There's some annoying edge conditions that could be gotten rid of if we
    could assume the stack contained integers or the like, replacing None with
    a sentinel scalar that can be compared directly.
    """
    temporary_stack = Stack()
    if not stack.empty:
        temporary_stack.push(stack.pop())

    while not stack.empty:
        current = stack.pop()
        top = temporary_stack.peek()

        while current < top:
            stack.push(temporary_stack.pop())
            top = temporary_stack.peek()
            if top is None:
                break

        temporary_stack.push(current)

    while not temporary_stack.empty:
        stack.push(temporary_stack.pop())
