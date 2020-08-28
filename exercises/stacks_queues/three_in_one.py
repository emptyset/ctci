"""
3.1
Describe how you could use a single array to implement three stacks.
"""


class NStack:
    """
    Assuming the array we're talking about is a classic C-style array, it can
    only hold one type of value, let's say integer.  If I were programming this
    in C, then I'd have the array hold integer pointers so that I can insert
    nulls into the array.  Since we're using python, we have list, so I can use
    None as a good representation for the scheme described below.

    The way the "three in one" stack would work is to use offset indexes for
    each stack.  So, stack 0 has values at array index 0, 3, 6, 9, etc.  Stack
    1 has values stored at array index 1, 4, 7, 10, etc.  This can actually be
    generalized to N stacks, so I'll implement this class below and have some
    tests around it.  The stack operations are:

    - push
    - pop
    - peek
    - size

    Each of these requires an additional parameter to specify the stack index.
    For each operation, special care is taken to note the current size and
    adjust the contents of the single list accordingly.
    """
    def __init__(self, N):
        if N == 0:
            raise ValueError

        self._N = N
        self._array = []

    def push(self, value, stack_index):
        if stack_index >= self._N:
            raise ValueError

        for index in range(stack_index, len(self._array), self._N):
            if self._array[index] is None:
                self._array[index] = value
                return

        # if we don't return, we need to append a new set of placeholders
        for index in range(0, self._N):
            if index == stack_index:
                self._array.append(value)
            else:
                self._array.append(None)

    def pop(self, stack_index):
        if stack_index >= self._N:
            raise ValueError

        top_index = len(self._array) - self._N + stack_index
        for index in range(top_index, stack_index - 1, -self._N):
            if self._array[index] is None:
                continue
            else:
                value = self._array[index]
                self._array[index] = None
                return value

        return None

    def peek(self, stack_index):
        if stack_index >= self._N:
            raise ValueError

        for index in range(stack_index, len(self._array), self._N):
            previous_value = None
            if self._array[index] is None:
                return previous_value

            previous_value = self._array[index]

        return None

    def size(self, stack_index):
        if stack_index >= self._N:
            raise ValueError

        size = 0
        for index in range(stack_index, len(self._array), self._N):
            if self._array[index] is None:
                return size
            size += 1

        return size
