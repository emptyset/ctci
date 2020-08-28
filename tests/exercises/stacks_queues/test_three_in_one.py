from exercises.stacks_queues.three_in_one import NStack


def test_NStack__operations():
    stacks = NStack(3)

    assert stacks.size(0) == 0
    stacks.push(100, 0)
    stacks.push(101, 0)
    stacks.push(102, 0)
    assert stacks.size(0) == 3
    assert stacks.pop(0) == 102
    assert stacks.size(0) == 2

    assert stacks.size(1) == 0
    stacks.push(200, 1)
    stacks.push(201, 1)
    stacks.push(202, 1)
    stacks.push(203, 1)
    assert stacks.size(0) == 2
    assert stacks.size(1) == 4
    assert stacks.pop(1) == 203
    assert stacks.size(1) == 3

    assert stacks.peek(2) is None
    stacks.push(300, 2)
    assert stacks.size(0) == 2
    assert stacks.size(1) == 3
    assert stacks.size(2) == 1
    assert stacks.pop(2) == 300
    assert stacks.pop(2) is None
    assert stacks.size(2) == 0
