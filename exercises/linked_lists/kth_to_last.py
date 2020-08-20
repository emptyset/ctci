"""
2.2
Implement an algorithm to find the kth to last element of a singly linked list.
"""


def get_kth_to_last(k, ll):
    """
    The total size of the linked list isn't known.  The library implementation
    does provide a tail pointer, and is doubly linked, but we'll ignore that
    for this exercise.

    An efficient way to find the end of the list is to advance a pointer,
    doubling the steps to advance until the end is reached.  This takes overall
    O(n) steps to reach the end of the linked list, because each element must
    be visited in order to reach the next element.

    Once the end is determined, a second iteration can follow that takes only
    O(n) steps to reach the kth to last element.

    I might revisit this later if I can think of a way to solve in a single
    pass with some tedious pointer arithmetic.
    """
    advancer = ll.head
    advancer_index = 0

    target = 1

    while advancer.next is not None:
        if advancer_index == target:
            target *= 2

        advancer = advancer.next
        advancer_index += 1

    # at the last element; handle invalid case
    if k > advancer_index:
        return None

    follower = ll.head
    follower_index = 0

    while follower_index < advancer_index - k:
        follower = follower.next
        follower_index += 1

    return follower.value
