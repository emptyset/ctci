from exercises.lib.linked_list import Element
from exercises.lib.linked_list import LinkedList


"""
3.6
An animal shelter, which holds only dogs and cats, operates on a strictly
"first in, first out" basis.  People must adopt either the "oldest" (based on
arrival time) of all animals at the shelter, or they can select whether they
would prefer a dog or a cat (and will receive the oldest animal of that type.)
They cannot select which specific animal they would like.  Create the data
structures to maintain this system and implement operations such as enqueue,
dequeue_any, dequeue_dog, and dequeue_cat.  You may use the built-in LinkedList
data structure.
"""


class Animal:
    def __init__(self, kind, name):
        self._kind = kind
        self._name = name

    @property
    def kind(self):
        return self._kind

    @property
    def name(self):
        return self._name


class AnimalShelter:
    """
    There are no restrictions on runtime.  The interesting operations are when
    a person specifies dog or cat specifically, as this requires maintaining
    the order of arrival for both dog and cat in the same queue.

    A specific dog or cat dequeue is a search and then removing that element
    from the queue.  Since a linked list can be used, we can splice out the
    specific dog or cat and fixup the queue.
    """
    def __init__(self, iterable=[]):
        self._ll = LinkedList(iterable)

    def enqueue(self, animal):
        self._ll.append(Element(animal))

    def dequeue_any(self):
        if len(self._ll) > 0:
            animal = self._ll.head.value
            self._ll.remove(self._ll.head)
            return animal
        else:
            return None

    def dequeue_cat(self):
        return self.dequeue_kind('cat')

    def dequeue_dog(self):
        return self.dequeue_kind('dog')

    def dequeue_kind(self, kind):
        for element in self._ll:
            if element.value.kind == kind:
                self._ll.remove(element)
                return element.value

        return None
