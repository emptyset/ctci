from exercises.stacks_queues.sort_stack import Stack
from exercises.stacks_queues.sort_stack import sort_stack


def test_sort_stack__initially_sorted():
    s = Stack()
    for index in range(5, 0, -1):
        s.push(index)

    sort_stack(s)
    for index in range(1, 6):
        assert index == s.pop()


def test_sort_stack__initially_reverse():
    s = Stack()
    for index in range(1, 6):
        s.push(index)

    sort_stack(s)
    for index in range(1, 6):
        assert index == s.pop()
