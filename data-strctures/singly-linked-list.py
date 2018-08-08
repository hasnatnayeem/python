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

    def insertAtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertAtEnding(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    
list = LinkedList()
n1 = Node('Node 1')
n2 = Node('Node 2')
n3 = Node('Node 3')
n4 = Node('Node 4')

list.head = n1
n1.next = n2
n2.next = n3
n3.next = n4

# Insert data at the beginning of the list
list.insertAtBeginning("Beginning")

# Insert data at the end of the list
list.insertAtEnding("Ending")

list.print()