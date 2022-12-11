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
            string += "{ " + str(current.value) + " } -> "
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

    def append(self, item):
        if not self.head:
            self.head = Node(item)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(item)

    def insert_before(self, target, item):
        current = self.head
        lag = None
        while current:
            if current.value == target:
                if lag is None:
                    self.insert(item)
                    return
                lag.next = Node(item)
                lag.next.next = current
                return
            lag = current
            current = current.next
        raise TargetError

    def insert_after(self, target, item):
        current = self.head
        while current:
            if current.value == target:
                temp = current.next
                current.next = Node(item)
                current.next.next = temp
                return
            current = current.next
        raise TargetError


class TargetError(Exception):
    pass


def zip_lists(list_a, list_b):
    zipped = LinkedList()
    current_a = list_a.head
    current_b = list_b.head
    while current_a or current_b:
        if current_a:
            zipped.append(current_a.value)
            current_a = current_a.next
        if current_b:
            zipped.append(current_b.value)
            current_b = current_b.next
    return zipped
