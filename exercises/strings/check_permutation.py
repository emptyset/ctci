'''
1.2
Given two strings, write a method to decide if one is a
permutation of the other.
'''


def check_permutation__via_sorting(left, right):
    '''
    Sorting the two strings and comparing directly is concise.
    However, the time complexity is O(n log n).
    '''
    left = list(left)
    left.sort()
    right = list(right)
    right.sort()

    return left == right


def check_permutation__via_hash(left, right):
    '''
    An alternative with time complexity O(n) trades space for time,
    by leveraging a hash map (or dict).
    After collecting a count of all characters from both strings, iterate over
    the counts and any odd number indicates an unmatched character.
    '''
    d = {}

    def insert(c, d):
        if c in d:
            d[c] = d[c] + 1
        else:
            d[c] = 1

    [insert(c, d) for c in left]
    [insert(c, d) for c in right]

    for count in d.values():
        if count % 2 != 0:
            return False

    return True
