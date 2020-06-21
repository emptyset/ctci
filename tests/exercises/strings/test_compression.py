from exercises.strings.compression import compress


def test_compress__compressed_results():
    assert compress('aabcccccaaa') == 'a2b1c5a3'
    assert compress('aaa') == 'a3'
    assert compress('cccccccccc') == 'c10'
    assert compress('AAAAAAaaaaaa') == 'A6a6'
    assert compress('abcdeeeeeee') == 'a1b1c1d1e7'


def test_compress__does_not_compress_well():
    assert compress('abcde') == 'abcde'
    assert compress('') == ''
    assert compress('a') == 'a'
    assert compress('aa') == 'aa'
    assert compress('aabbccddee') == 'aabbccddee'
    assert compress('abcdeeeeee') == 'abcdeeeeee'
