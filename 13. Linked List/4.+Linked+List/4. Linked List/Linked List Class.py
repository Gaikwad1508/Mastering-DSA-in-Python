class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtHead(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        return self.head

    def insertAtIndex(self,data,index):
        if index == 0:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
            return self.head
        if self.head is None:
            print('index is out of bounds')
            return self.head

        count = 0
        temp = self.head
        while temp is not None and count < index -1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Index out of bounds, please check index")
            return self.head
        newNode = Node(data)
        newNode.next = temp.next
        temp.next = newNode
        return self.head
    
    # Remove
    def deleteAtHead(self):
        if self.head is None:
            return None
        self.head = self.head.next
        return self.head
    
    def deleteAtTail(self):
        if self.head is None or self.head.next is None:
            self.head = None
            return None
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        return self.head
    
    def deleteAtIndex(self, index):
        if self.head is None:
            print("List is empty")
            return self.head
        
        if index == 0:
            return self.head.next
        
        self.head.next = self.deleteAtIndex(self.head.next, index - 1)
        return self.head

    # Search
    def search(self, data):
        if self.head is None:
            return "not found"
        index = 0
        temp = self.head
        while temp != None:
            if temp.data == data:
                return index
            temp = temp.next
            index += 1
        return "Not Found"
    
    # Update 
    def updateNode(self,valToUpdate,index):
        count = 0
        temp = self.head
        while temp!=None and count < index:
            temp = temp.next
            count += 1
        if temp is None:
            print("index out of bounds")
            return self.head
        temp.data = valToUpdate
        return self.head


    def print_LL(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end= " -> ")
            temp = temp.next
        print()
        return

    def length_LL(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count


ll1 = LinkedList()

ll1.insertAtHead(10)
ll1.insertAtHead(20)
ll1.insertAtHead(30)
ll1.insertAtHead(40)
head = ll1.insertAtHead(50)

ll1.print_LL()
ll1.insertAtIndex(60, 2)
ll1.print_LL()
print(ll1.search(30))
ll1.updateNode(17, 3)
ll1.print_LL()