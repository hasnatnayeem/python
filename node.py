class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

n1 = Node('Node 1')
n2 = Node('Node 2')
n3 = Node('Node 3')
n4 = Node('Node 4')
n5 = Node('Node 5')
n6 = Node('Node 6')

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

head = n1


// Traversing
while head:
    print(head.value)
    head = head.next

