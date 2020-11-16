from collections import deque

"""
4.10
T1 and T2 are two very large binary trees, with T1 much bigger than T2.  Create
an algorithm to determine if T2 is a subtree of T1.

A tree T2 is a subtree of T1 if there exists a node n in T1 such that the
subtree of n is identical to T2.  That is, if you cut off the tree at node n,
the two trees would be identical.
"""


def check(t1, t2):
    """
    The problem doesn't call for a binary search tree.  :(

    In this case, something we could do is a sort of "string matching as you
    go" method.  We have to exhaustively search the nodes at T1 in a preorder
    traversal to locate a match with T2's root "character".  T2 is traversed in
    a preorder traversal to come up with a "substring", and as we traverse T1,
    we see if there is alignment as each node is visited.

    However, this is not sufficient.  We actually have to examine the
    structure; different trees can produce the same preorder traversal.  If we
    include the empty/null/None leaves, then we will be able to verify the
    "strings" are a match - we can treat empty/null/None leaves as "spaces".

    Because we don't have guarantees of "character" uniqueness, if we're just
    moving along, it's possible we could have to backtrack to a second match on
    T2's root "character" when encountered.  To avoid this, we can fix the T1
    search pointer to the current subtree root candidate "character" and
    collect the "string" by taking size(T2) node values from T1, from this
    pointer.  If the "string" match fails, we can continue the search.

    The algorithm operates in O(n*m) time where n is the size of T1 and m is
    the size of T2, and it is space efficient.
    """
    if t2 is None:
        return True

    if t1 is None:
        return False

    substring = stringify(t2)
    limit = len(substring)

    nodes = deque([t1])

    while len(nodes) > 0:
        current = nodes.popleft()

        if current.value == substring[0]:
            candidate = stringify(current, limit)
            if candidate == substring:
                return True
        else:
            if current.left is not None:
                nodes.append(current.left)

            if current.right is not None:
                nodes.append(current.right)

    return False


def stringify(root, limit=None):
    result = []

    if root is None:
        result.append(None)
    else:
        if limit is None:
            result.append(root.value)
            result.extend(stringify(root.left))
            result.extend(stringify(root.right))
        else:
            nodes = deque([root])
            while len(nodes) > 0 and limit > 0:
                current = nodes.popleft()
                result.append(current.value)
                limit -= 1

                if current.left is None:
                    result.append(None)
                    limit -= 1
                else:
                    nodes.append(current.left)

                if current.right is None:
                    result.append(None)
                    limit -= 1
                else:
                    nodes.append(current.right)

    return result
