from exercises.strings.urlify import urlify


def test_urlify__empty():
    assert urlify('', 0) == ''


def test_urlify__edge_case():
    assert urlify(' a  ', 4) == '%20a'


def test_urlify__typical():
    s = 'all animals are created equal        '
    assert urlify(s, 37) == 'all%20animals%20are%20created%20equal'
