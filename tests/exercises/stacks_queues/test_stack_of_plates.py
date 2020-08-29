from exercises.stacks_queues.stack_of_plates import SetOfStacks


def test_SetOfStacks__operations():
    s = SetOfStacks(2)
    assert s.capacity == 2
    assert s.pop() is None

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    assert s.pop() == 5
    assert s.pop() == 4
    assert s.popAt(0) == 2
    assert s.popAt(0) == 1
    assert s.popAt(0) == 3
    assert s.pop() is None
