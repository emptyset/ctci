from exercises.strings.is_unique import is_unique__using_set
from exercises.strings.is_unique import is_unique__no_data_structures


def test_is_unique__yes():
    s = 'xenuphobia'
    assert is_unique__using_set(s)
    assert is_unique__no_data_structures(s)


def test_is_unique__yes_single_char():
    s = 'a'
    assert is_unique__using_set(s)
    assert is_unique__no_data_structures(s)


def test_is_unique__yes_empty():
    s = ''
    assert is_unique__using_set(s)
    assert is_unique__no_data_structures(s)


def test_is_unique__no():
    s = 'xenophobia'
    assert not is_unique__using_set(s)
    assert not is_unique__no_data_structures(s)
