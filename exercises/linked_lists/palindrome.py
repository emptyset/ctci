"""
2.6
Implement a function to determine if a linked list is a palindrome.
"""


def is_palindrome(ll):
    """
    This can be accomplished in O(n) by using a stack and a second pass over
    the linked list.
    """
    stack = []
    for element in ll:
        stack.append(element.value)

    test = True
    for element in ll:
        test &= element.value == stack.pop()

    return test
