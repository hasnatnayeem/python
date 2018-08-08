class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def printItems(self):
        for data in self.items:
            print(data)


stack = Stack()
stack.push(13)
stack.push(5)
stack.push(23)
stack.push(33)
stack.pop()
stack.printItems()
