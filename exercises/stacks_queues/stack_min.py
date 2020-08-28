"""
3.2
How would you design a stack which, in addition to push and pop, has a function
min which returns the minimum element?  Push, pop, and min should all operate
in O(1) time.
"""


class MinStack:
    """
    The trick to this implementation is to record the minimum value at every
    time.  A quick way to accomplish this is to push a tuple to the stack,
    where the first value of the tuple is the value pushed to the stack, and
    the second value is the current minimum in the stack.  This way, when you
    pop, you always have the minimum value just by looking at the top value.

    You can't just use a single variable to store the minimum value, because
    then when you pop, the minimum value is no longer valid, so you have to
    discover the minimum value by traversing the stack, so it's no longer an
    O(1) operation.
    """
    def __init__(self):
        self._stack = []
        self._size = 0

    def push(self, value):
        minimum = self.min
        if minimum is None or value < minimum:
            self._stack.append((value, value))
        else:
            self._stack.append((value, minimum))

        self._size += 1

    def pop(self):
        if self._size == 0:
            return None

        self._size -= 1
        return self._stack.pop()[0]

    @property
    def min(self):
        if self._size == 0:
            return None

        return self._stack[self._size - 1][1]
