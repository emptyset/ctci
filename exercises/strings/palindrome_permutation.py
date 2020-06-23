"""
1.4
Given a string, write a function to check if it is a permutation of a
palindrome.
"""


def check__via_sort(s):
    """
    A straightforward approach is to sort the string, and then push the
    characters onto a stack, popping the top element if there is a match.
    Finally, test if the stack size is not greater than one.
    However, due to the sort, this algorithm executes in O(n log n) time.
    """
    s_list = list(s)
    s_list.sort()

    stack = []
    for index in range(0, len(s_list)):
        c = s_list[index]

        if c.isspace():
            continue

        if len(stack) > 0:
            top = stack.pop()
            if c != top:
                stack.append(top)
                stack.append(c)
        else:
            stack.append(c)

    return len(stack) <= 1


def check__via_hash(s):
    """
    Another approach is to use a hash as a kind of bucket sort.
    Push each character in the string as a key to the hash.
    If the key is already present, delete the key.
    Finally, test if there is no more than one key in the hash.
    This algorithm runs in O(n).
    """
    buckets = {}

    for c in s:
        if c.isspace():
            continue

        if c in buckets:
            del buckets[c]
        else:
            buckets[c] = None

    return len(buckets.keys()) <= 1
