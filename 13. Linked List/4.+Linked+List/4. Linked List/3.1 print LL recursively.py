class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

head = node1
node1.next = node2
node2.next = node3

def printData(head):
    if not head:
        return
    
    print(head.data)
    printData(head.next)

printData(head)