from exercises.strings.one_away import is_one_away


def test_is_one_away__remove():
    assert is_one_away('pale', 'ale')
    assert is_one_away('pale', 'ple')
    assert is_one_away('pale', 'pal')
    assert is_one_away('p', '')
    assert is_one_away('pale', 'pale')
    assert is_one_away('', '')
    assert not is_one_away('pale', 'al')


def test_is_one_away__insert():
    assert is_one_away('hush', 'shush')
    assert is_one_away('', 'h')
    assert is_one_away('cat', 'cats')
    assert is_one_away('cat', 'chat')
    assert not is_one_away('lam', 'slams')


def test_is_one_away__replace():
    assert is_one_away('pish', 'posh')
    assert is_one_away('sand', 'band')
    assert is_one_away('sans', 'sand')
    assert not is_one_away('pale', 'fire')
