class LinkedList:
    """
    Implements a doubly-linked list.
    """
    def __init__(self, iterable):
        """
        Initialized from a python iterable.
        """
        self._head = None
        self._tail = None

        current = None
        for value in iterable:
            element = Element(value)

            if self.head is None:
                current = element
                self.head = current
            else:
                element.prev = current
                current.next = element
                current = element

        self.tail = current

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = value

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, value):
        self._tail = value

    @property
    def values(self):
        for element in self:
            yield element.value

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __len__(self):
        length = 0
        for element in self:
            length += 1
        return length

    def __getitem__(self, index):
        if index < 0:
            return None

        current = self.head
        i = 0
        while i < index:
            current = current.next
            i += 1

        return current


class Element:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self._prev = prev
        self._next = next

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, element):
        self._prev = element

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, element):
        self._next = element
