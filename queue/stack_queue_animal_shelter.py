from .queue import Queue


class AnimalShelter:
    def __init__(self):
        self.q = Queue()

    def enqueue(self, animal):
        self.q.enqueue(animal)
    
    def dequeue(self, pref):
        valid = pref == "dog" or pref == "cat"
        if not valid:
            return None
        current = self.q.front
        lag = None
        dequeued = None
        while current:
            if current.value.type == pref:
                if current == self.q.front:
                    return self.q.dequeue()
                dequeued = current
                lag.next = current.next
            lag = current
            current = current.next
        return dequeued.value


class Dog:
    def __init__(self):
        self.type = "dog"


class Cat:
    def __init__(self):
        self.type = "cat"

