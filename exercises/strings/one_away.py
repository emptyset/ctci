"""
1.5
There are three types of edits that can be performed on strings: insert a
character, remove a character, or replace a character.  Given two strings,
write a function to check if they are one edit (or zero edits) away.
"""


def is_one_away(left, right):
    """
    The basic idea is to immediately classify the expected operation.
    For example, if the left string is 1 longer than the right, then this
    is a REMOVE operation.  If right is 1 longer than left, this means
    we expect an INSERT.  If the strings are equal, we can expect at most
    one REPLACE.

    The strings are treated as queues, and iterated over in tandem.  When
    there is a mismatch, depending on our expected operation, we .pop(0)
    on each string appropriately.  For example, if we encounter a mismatch,
    and we expected a REMOVE, then we .pop(0) on the left string.

    If another mismatch is encountered, we can exit immediately with False.
    When the end of both strings is reached, we return True.
    There"s some additional checks for the empty string edge cases.

    Complexity is O(n).

    I had some initial problems with this because I took the approach of
    iterating over the strings in tandem first; and what happens is that it
    becomes tricky to classify the operation and perform the "extra" dequeue,
    given some of the edge cases I came up with.  If you iterate over the
    strings in tandem, you can "classify" the operation needed to shift either
    the left or right string by sliding a "window" of two characters.  In an
    earlier solution attempt, this required handling the edge cases specially
    and also padding the strings at the end to ensure the "window" didn"t run
    over.

    Instead of the list conversion to treat the strings as queues, one can
    also use indexes and implement the operations as increments, I just don"t
    like the tedious index math around the edge cases.
    """
    def REMOVE(left, right):
        if len(left) > 0:
            _ = left.pop(0)

    def INSERT(left, right):
        if len(right) > 0:
            _ = right.pop(0)

    def REPLACE(left, right):
        if len(left) > 0 and len(right) > 0:
            _ = left.pop(0)
            _ = right.pop(0)

    def classify_op(left, right):
        if len(left) == len(right):
            return REPLACE
        elif len(left) == len(right) + 1:
            return REMOVE
        elif len(left) == len(right) - 1:
            return INSERT
        else:
            return None

    op = classify_op(left, right)

    if op is None:
        return len(left) == len(right)

    left = list(left)
    right = list(right)
    ops = 0

    while len(left) > 0 and len(right) > 0:
        left_char = left[0]
        right_char = right[0]

        if left_char != right_char:
            op(left, right)
            ops = ops + 1

        if ops > 1:
            return False

        if len(left) < 1 or len(right) < 1:
            break

        left.pop(0)
        right.pop(0)

    return True
