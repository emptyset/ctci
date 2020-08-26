from collections import defaultdict

from exercises.lib.linked_list import Element
from exercises.lib.linked_list import LinkedList


"""
2.5
You have two numbers represented by a linked list, where each node contains a
single digit.  The digits are stored in reverse order, such that the 1's digit
is at the head of the list.  Write a function that adds the two numbers and
returns the sum as a linked list.
"""


def sum(left, right, reverse=True):
    """
    Summation of digits may "carry over" a value to the next digit place.

    When evaluating the linked list, it's simple to just take the carry along
    the traversal of both left and right in tandem, and apply it to the next
    digit place.  If one list terminates before the other, the carry gets
    applied just the same until the traversal ends for the longer list.  This
    algorithm runs in O(M+N) time where M, N is the length of left, right
    respectively.  The sum of each individual element can be applied into a new
    element and just appended to a new linked list.

    The non-reversed case is a bit trickier, and requires special handling for
    the possibility of non-equal list lengths, as we can't assume the first
    elements are the same digit place.  Once we determine the maximum length,
    we can use a hash to store each digit place keyed by power of 10.  Using
    the hash allows us to keep the runtime to O(M+N) at the cost of
    O(max(M, N)) space.  Other methods involve complicated back-tracking with
    pointers, or using a stack which is essentially the first method.

    The non-reserved solution avoids fun workarounds like reversing the linked
    list and running the first algorithm, or converting the LinkedList into
    numbers, summing those, and then converting the number into a string and
    then passing it directly into LinkedList... :rolling_on_the_floor_laughing:
    """
    result = LinkedList([])
    if reverse:
        current_left = left.head
        current_right = right.head

        carry = 0
        while current_left is not None and current_right is not None:
            left_value = 0
            if current_left is not None:
                left_value = current_left.value
                current_left = current_left.next

            right_value = 0
            if current_right is not None:
                right_value = current_right.value
                current_right = current_right.next

            total = left_value + right_value + carry
            carry = total // 10
            digit = total % 10
            result.append(Element(digit))

        if carry > 0:
            result.append(Element(carry))
    else:
        # this is needed here in case there is carry past the max digit place
        places = defaultdict(lambda: 0)

        for ll in [left, right]:
            for index, element in enumerate(ll):
                place = len(ll) - index - 1
                places[place] += element.value

        for place in sorted(places.keys()):
            carry = places[place] // 10
            places[place] %= 10
            if carry > 0:
                places[place + 1] += carry

        for place in sorted(places.keys(), reverse=True):
            result.append(Element(places[place]))

    return result
