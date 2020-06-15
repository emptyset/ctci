'''
1.1
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
'''


def is_unique__using_set(s):
    '''
    Using a set (or dictionary) is concise.
    '''
    return len(s) == len(set(s))


def is_unique__no_data_structures(s):
    '''
    Generally, this calls for a sorting algorithm; using the builtin here.
    Complexity is effectively O(n log n) [+ O(n)].
    If tasked to implement a sort, I recommend a recursive mergesort which is
    easier to produce under time constraints.
    Using two pointers traverses the list until the same character is
    detected, indicating that there is a duplicate present.
    '''
    if len(s) <= 1:
        return True

    s_list = list(s)
    s_list.sort()

    lead = 1
    follow = 0

    while lead < len(s_list):
        if s_list[follow] == s_list[lead]:
            return False
        lead = lead + 1
        follow = follow + 1

    return True
