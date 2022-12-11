class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        if not self.head:
            return "NULL"
        current = self.head
        string = ""
        while current:
            string += "{ " + current.value + " } -> "
            current = current.next
        string += "NULL"
        return string

    def insert(self, item):
        old = self.head
        self.head = Node(item)
        self.head.next = old

    def includes(self, item):
        current = self.head
        while current:
            if current.value == item:
                return True
            current = current.next
        return False

    def kth_from_end(self, k):
        current = self.head
        lag = self.head
        while current.next:
            if k:
                k -= 1
            else:
                lag = lag.next
            current = current.next
        if k:
            raise TargetError
        return lag.value

class TargetError(Exception):
    pass