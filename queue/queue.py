class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self, front=None):
        self.front = front

    def enqueue(self, item):
        if self.front is None:
            self.front = Node(item)
            return
        current = self.front
        while current.next:
            current = current.next
        current.next = Node(item)

    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError
        dequeued = self.front
        self.front = self.front.next
        return dequeued.value

    def peek(self):
        if self.front is None:
            raise InvalidOperationError
        return self.front.value

    def is_empty(self):
        return self.front is None


class InvalidOperationError(Exception):
    pass