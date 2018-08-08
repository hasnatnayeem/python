class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

items = Queue()
items.enqueue(1)
items.enqueue(2)
items.enqueue(3)

print(items.dequeue())
print(items.dequeue())
print(items.dequeue())
