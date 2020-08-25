from exercises.lib.linked_list import Element
from exercises.lib.linked_list import LinkedList


"""
2.4
Write code to partition a linked list around a value x, such that all nodes
less than x come before all nodes greater than or equal to x.  If x is
contained within the list, the values of x only need to be right after the
elements less than x.  The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right
partitions.
"""


def partition(ll, p):
    """
    Admittedly, much of the implementation magic here is making sure that the
    basic dunder method __add__ to join two linked lists works correctly.  I
    also rewrote the LinkedList initializer slightly to make use of a new
    append method that appends an Element to the end of a LinkedList and
    adjusts the prev/next pointers and the tail pointer correctly.
    """
    left = LinkedList([])
    right = LinkedList([])
    for value in ll.values:
        element = Element(value)
        if value < p:
            left.append(element)
        else:
            right.append(element)

    return left + right
