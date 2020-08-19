"""
1.9
Assume you have a method isSubstring which checks if one word is a substring of
another.  Given two strings, s1 and s2, write code to check if s2 is a rotation
of s1 using only one call to isSubstring (e.g. "waterbottle" is a rotation of
"erbottlewat").
"""


def is_rotation(s1, s2):
    """
    At first glance, the limitation of only calling isSubstring once seems to
    imply that this is the final test after rotating s2 to "align" with s1.

    But how do I know when the string is aligned?  Especially for strings
    consisting of only two characters...

    Any substring of two or more characters can be split arbitrarily by the
    rotation.

    One dead-end idea is to create a hashing function that somehow preserves
    the ordering information.  After thinking about that for a minute, I
    decided to shelve that approach in favor of the following:

    s1 =         waterbottle
    s2 = erbottlewaterbottlewat

    By repeating one of the strings sequentially, and testing the other via
    isSubstring, we arrive at the answer.  This works because we have "rolled
    out" one of the strings (rotation is kind of like treating the string like
    a circular linked list) and so if the other string is a substring, this
    means that the rolled out string is a rotation.

    We can use the built-in string.find to represent the isSubstring function.
    """
    rollout = s2 + s2
    return rollout.find(s1) >= 0
