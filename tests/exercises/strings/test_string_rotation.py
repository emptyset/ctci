from exercises.strings.string_rotation import is_rotation


def test_is_rotation__yes():
    assert is_rotation('waterbottle', 'erbottlewat')
    assert is_rotation('abbaabba', 'aabbaabb')
    assert is_rotation('funusual', 'usualfun')
    assert is_rotation('abbababba', 'bababbaab')
    assert is_rotation('catpower', 'powercat')


def test_is_rotation__no():
    assert not is_rotation('waterbottle', 'bottlewatre')
    assert not is_rotation('ababababababababababab', 'abababababbbababababab')
    assert not is_rotation('tacopower', 'opowercat')
