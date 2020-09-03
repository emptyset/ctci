from collections import deque
from dataclasses import dataclass

from exercises.lib.tree import BinaryNode


"""
4.2
Given a sorted (increasing order) array with unique integer elements, write an
algorithm to create a binary search tree with minimal height.
"""


def to_bst(array):
    """
    One way to approach this problem is to pick the middle value, and then
    recursively build the BST from the root down by picking middle values for
    the left and the right of the root.  This can be a bit tedious by having to
    perform index arithmetic, and I hate index arithmetic.

    One thing that is nice about the question is that we are given a total
    ordering, so this means that for any element in the array, we have a
    guarantee that the previous element is less than, and the next element is
    greater than, strictly.

    This allows us to build the BST in layers, like a cake.  In the first pass,
    every other element in the array is taken and these become the leaf nodes
    of our BST.  They are added to an "orphans" queue.  In the next pass, we
    take every other element again, only this time, it checks the orphans queue
    to assign left and right nodes.

    I think the runtime is something like O(log^2 n) because we make at most
    log n passes over the number of elements, but each time, we are only
    working with half the number of elements from the previous step.
    """
    @dataclass
    class MarkedElement:
        value: object
        marked: bool = False

    elements = [MarkedElement(value=v) for v in array]
    orphans = deque([])

    def unmarked(elements):
        return list(filter(lambda e: not e.marked, elements))

    parents = deque([])
    while len(unmarked(elements)) > 0:
        for index, element in enumerate(unmarked(elements)):
            if index % 2 == 0:
                element.marked = True
                parent = BinaryNode(
                    element.value,
                    left=safe_popleft(orphans),
                    right=safe_popleft(orphans))
                parents.append(parent)

        parents.reverse()
        orphans.extendleft(parents)
        parents.clear()

    # the final orphan is the root of the tree
    root = safe_popleft(orphans)
    return root


def safe_popleft(queue):
    """
    Python's deque throws IndexError when you pop* because it supports None as
    a valid item in the queue.  However, it's not possible to use None as a
    valid item if the input to the queue came from a total ordering.
    """
    if len(queue) > 0:
        return queue.popleft()
    else:
        return None
