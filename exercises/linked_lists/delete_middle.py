"""
2.3
Implement an algorithm to delete a node in the middle (i.e. any node but the
first and last node, not necessarily the exact middle) of a singly linked list,
given only access to that node.
"""


def delete(ll, element):
    """
    Set up two pointers, an advancer and a follower.  When the advancer matches
    the element reference, adjust prev/next pointers on the elements.
    """
    # per the question instructions
    assert len(ll) > 2

    advancer = ll[1]
    follower = ll[0]

    while advancer is not None:
        if advancer == element:
            follower.next = advancer.next
            advancer.next.prev = follower
            break

        advancer = advancer.next
        follower = follower.next
