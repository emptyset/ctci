"""
3.3
Imagine a (literal) stack of plates.  If the stack gets too high, it might
topple.  Therefore, in real life, we would like to start a new stack when the
previous stack exceeds some threshold.  Implement a data structure SetOfStacks
that mimics this.  SetOfStacks should be composed of several stacks and should
create a new stack once the previous one exceeds capacity.  SetOfStacks.push()
and SetOfStacks.pop() should behave identically to a single stack (that is,
pop() should return the same values as it would if there were just a single
stack.)

Implement a function popAt(int index) which performs a pop operation on a
specific sub-stack.
"""


class SetOfStacks:
    """
    The implementation here is very straightforward, it's just a lot of
    housekeeping around where the top of the stack is at any point.
    """
    def __init__(self, capacity):
        self._set = []
        self._set.append([])
        self._capacity = capacity

    @property
    def capacity(self):
        return self._capacity

    @property
    def _substack(self):
        return self._set[len(self._set) - 1]

    def push(self, value):
        if len(self._substack) == self._capacity:
            self._set.append([])
        self._substack.append(value)

    def pop(self):
        if len(self._substack) == 0:
            if len(self._set) == 1:
                return None

            self._set.pop()

        return self._substack.pop()

    def popAt(self, index):
        """
        The behavior is a bit unspecified, but I think the expectation would be
        to always return a value, so that None always means the set of stacks
        is empty.  This means if a pop() on a substack empties it, then the
        substack should be deleted from the set of stacks.
        """
        if index < 0 or index >= len(self._set):
            raise ValueError

        substack = self._set[index]
        value = substack.pop()

        if len(substack) == 0 and len(self._set) > 1:
            del self._set[index]

        return value
