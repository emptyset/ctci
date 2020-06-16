from exercises.strings.palindrome_permutation import check__via_sort
from exercises.strings.palindrome_permutation import check__via_hash


def test_check__empty():
    assert check__via_sort('')
    assert check__via_hash('')


def test_check__solo():
    assert check__via_sort('z')
    assert check__via_hash('a')


def test_check__yes():
    assert check__via_sort('do geese see god')
    assert check__via_sort('geese do see god')
    assert check__via_sort('eva can i stab bats in a cave')
    assert check__via_sort('eva i can stab bats in a cave')
    assert check__via_hash('do geese see god')
    assert check__via_hash('geese do see god')
    assert check__via_hash('eva can i stab bats in a cave')
    assert check__via_hash('eva i can stab bats in a cave')


def test_check__no():
    assert not check__via_sort('detartrate')
    assert not check__via_hash('tattarrattap')
