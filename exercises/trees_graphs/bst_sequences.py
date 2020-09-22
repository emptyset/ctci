"""
4.9
A binary search tree was created by traversing through an array from left to
right and inserting each element.  Given a binary search tree with distinct
elements, print all possible arrays that could have led to this tree.
"""


def source_arrays(node):
    """
    I worked on this problem for an hour, and I'm stumped at the moment, so
    this is the first CTCI exercise I'm intentionally skipping.

    The first thing to recognize is that we can build the tree in almost any
    order, from the root on down.  To illustrate this, let's say we have a root
    T with children L and R.  Two possible source arrays are:

    [ T, L subtree, R subtree ]
    [ T, R subtree, L subtree ]

    But note that also we can have:

    [ T, L, L-L subtree, L-R subtree, R, R-L subtree, R-R subtree ]

    In any order where the only restriction is that L is before L-* and R
    before R-* ... and so on.  This is the full set worked out by hand:

    [ T, L, L-L, L-R, R, R-L, R-R ] # 54 total possible top-level arrangements
    [ T, L, L-L, L-R, R, R-R, R-L ]

    [ T, L, L-L, R, L-R, R-L, R-R ]
    [ T, L, L-L, R, L-R, R-R, R-L ]
    [ T, L, L-R, R, L-L, R-L, R-R ]
    [ T, L, L-R, R, L-L, R-R, R-L ]

    [ T, L, L-L, R, R-L, L-R, R-R ]
    [ T, L, L-L, R, R-R, L-R, R-L ]
    [ T, L, L-R, R, R-L, L-L, R-R ]
    [ T, L, L-R, R, R-R, L-L, R-L ]

    [ T, L, L-L, R, R-L, R-R, L-R ]
    [ T, L, L-L, R, R-R, R-L, L-R ]
    [ T, L, L-R, R, R-L, R-R, L-L ]
    [ T, L, L-R, R, R-R, R-L, L-L ]

    [ T, L, R, L-L, L-R, R-L, R-R ]
    [ T, L, R, L-L, L-R, R-R, R-L ]
    [ T, L, R, L-R, L-L, R-L, R-R ]
    [ T, L, R, L-R, L-L, R-R, R-L ]

    [ T, R, L, L-L, L-R, R-L, R-R ]
    [ T, R, L, L-L, L-R, R-R, R-L ]
    [ T, R, L, L-R, L-L, R-L, R-R ]
    [ T, R, L, L-R, L-L, R-R, R-L ]

    [ T, L, R, L-L, R-L, L-R, R-R ]
    [ T, L, R, L-L, R-R, L-R, R-L ]
    [ T, L, R, L-R, R-L, L-L, R-R ]
    [ T, L, R, L-R, R-R, L-L, R-L ]

    [ T, R, L, L-L, R-L, L-R, R-R ]
    [ T, R, L, L-L, R-R, L-R, R-L ]
    [ T, R, L, L-R, R-L, L-L, R-R ]
    [ T, R, L, L-R, R-R, L-L, R-L ]

    [ T, L, R, L-L, R-L, R-R, L-R ]
    [ T, L, R, L-L, R-R, R-L, L-R ]
    [ T, L, R, L-R, R-L, R-R, L-L ]
    [ T, L, R, L-R, R-R, R-L, L-L ]

    [ T, R, L, L-L, R-L, R-R, L-R ]
    [ T, R, L, L-L, R-R, R-L, L-R ]
    [ T, R, L, L-R, R-L, R-R, L-L ]
    [ T, R, L, L-R, R-R, R-L, L-L ]

    [ T, L, R, R-L, L-L, R-R, L-R ]
    [ T, L, R, R-R, L-L, R-L, L-R ]
    [ T, L, R, R-L, L-R, R-R, L-L ]
    [ T, L, R, R-L, L-R, R-L, L-L ]

    [ T, R, L, R-L, L-L, R-R, L-R ]
    [ T, R, L, R-R, L-L, R-L, L-R ]
    [ T, R, L, R-L, L-R, R-R, L-L ]
    [ T, R, L, R-L, L-R, R-L, L-L ]

    [ T, L, R, R-L, R-R, L-L, L-R ]
    [ T, L, R, R-R, R-L, L-L, L-R ]
    [ T, L, R, R-L, R-R, L-R, L-L ]
    [ T, L, R, R-L, R-L, L-R, L-L ]

    [ T, R, L, R-L, R-R, L-L, L-R ]
    [ T, R, L, R-R, R-L, L-L, L-R ]
    [ T, R, L, R-L, R-R, L-R, L-L ]
    [ T, R, L, R-L, R-L, L-R, L-L ]

    An easy way to map these derangements to a data structure that can be
    tracked across some kind of recursion or traversal of the BST is not
    immediately apparent to me.

    It feels similar to enumerating all depth-first traversals of the tree,
    except that it is definitely not: all depth-first traversals are "rooted"
    when being enumerated, and we have shown that the source array can "skip"
    over a subtree as long as the top-level ordering is preserved.
    """
    pass
