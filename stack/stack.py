class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self, top=None):
        self.top = top
    
    def push(self, item):
        if self.top is None:
            self.top = Node(item)
            return
        old = self.top
        self.top = Node(item)
        self.top.next = old

    def pop(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        popped = self.top
        self.top = self.top.next
        return popped.value

    def is_empty(self):
        return self.top is None
    
    def peek(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value


class PseudoQueue:
    def __init__(self):
        self.s_main = Stack()
        self.s_temp = Stack()

    def enqueue(self, item):
        self.s_main.push(item)
    
    def dequeue(self):
        if self.s_main.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        while self.s_main.top:
            self.s_temp.push(self.s_main.pop())
        dequeued = self.s_temp.pop()
        while self.s_temp.top:
            self.s_main.push(self.s_temp.pop())
        return dequeued


class InvalidOperationError(Exception):
    def __init__(self, value):
        self.value = value


def multi_bracket_validation(brackets):
    pairs = {
        "]": "[",
        ")": "(",
        "}": "{"
    }
    s = Stack()
    for i in brackets:
        if i in pairs.values():
            s.push(i)
            continue
        if s.is_empty():
            return False
        popped = s.pop()
        if popped != pairs[i]:
            return False
    return True
