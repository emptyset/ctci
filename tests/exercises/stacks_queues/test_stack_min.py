from exercises.stacks_queues.stack_min import MinStack


def test_MinStack__operations():
    s = MinStack()
    assert s.min is None

    s.push(7)
    assert s.min == 7

    s.push(9)
    assert s.min == 7

    s.push(5)
    assert s.min == 5

    s.push(12)
    assert s.min == 5

    s.push(1)
    assert s.min == 1

    s.pop()
    assert s.min == 5

    s.pop()
    s.pop()
    assert s.min == 7

    s.pop()
    s.pop()
    assert s.min is None
