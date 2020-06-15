from exercises.strings.check_permutation import check_permutation__via_sorting
from exercises.strings.check_permutation import check_permutation__via_hash


def test_check_permutation__yes():
    left = 'dungeons, and dragons'
    right = 'danged dragoons, nuns'
    assert check_permutation__via_sorting(left, right)
    assert check_permutation__via_hash(left, right)


def test_check_permutation__yes_empty():
    left = ''
    right = ''
    assert check_permutation__via_sorting(left, right)
    assert check_permutation__via_hash(left, right)


def test_check_permutation__no():
    left = "it's not for me to say"
    right = "wonderful! wonderful!"
    assert not check_permutation__via_sorting(left, right)
    assert not check_permutation__via_hash(left, right)
