from exercises.lib.linked_list import LinkedList

from exercises.linked_lists.palindrome import is_palindrome


def test_is_palindrome__empty():
    assert is_palindrome(LinkedList(''))


def test_is_palindrome__solo():
    assert is_palindrome(LinkedList('z'))


def test_is_palindrome__yes():
    assert is_palindrome(LinkedList('doomanevildeedlivenamood'))
    assert is_palindrome(LinkedList('drabasafoolaloofasabard'))


def test_is_palindrome__no():
    assert not is_palindrome(LinkedList('this is a palindrome'))
