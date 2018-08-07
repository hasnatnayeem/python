class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    
list = LinkedList()
n1 = Node('Node 1')
n2 = Node('Node 2')
n3 = Node('Node 3')
n4 = Node('Node 4')

list.head = n1
n1.next = n2
n2.next = n3
n3.next = n4

list.print()