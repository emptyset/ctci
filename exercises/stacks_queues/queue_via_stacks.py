"""
3.4
Implement a MyQueue class which implements a queue using two stacks.
"""


class StackQueue:
    """
    Since there are no runtime restrictions, the straight-forward
    implementation is to use the second stack as part of the dequeue operation.
    Every item in the queue is pop'd and push'd to the second stack, then we
    are able to pop the top element, and then "re-stack" the items in the first
    stack.
    """
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, item):
        self.enqueue_stack.append(item)

    def dequeue(self):
        for _ in range(0, len(self.enqueue_stack)):
            self.dequeue_stack.append(self.enqueue_stack.pop())

        item = None
        if len(self.dequeue_stack) > 0:
            item = self.dequeue_stack.pop()

        for _ in range(0, len(self.dequeue_stack)):
            self.enqueue_stack.append(self.dequeue_stack.pop())

        return item
