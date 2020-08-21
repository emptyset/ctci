from exercises.lib.linked_list import LinkedList


"""
2.1
Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?
"""


def remove_dupes__using_set(ll):
    """
    The naive approach is to use a set to add values and then just return the
    values from the set.  This is O(n).
    """
    return LinkedList(set(ll.values))


def remove_dupes__no_buffer(ll):
    """
    Without using the hash, sorting in-place is the way to do it.

    Just using built-in sort here, O(n log n) overall.
    """
    sll = LinkedList(sorted(ll.values))
    current = sll.head
    while current.next is not None:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next

    return sll
