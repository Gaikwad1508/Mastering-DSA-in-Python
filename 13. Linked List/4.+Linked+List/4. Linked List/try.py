class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
def print_LL(head):
    if head is None:
        return
    
    print(head.data, end = "->")
    print_LL(head.next)

def take_input():
    value = int(input("Enter the value of Node (-1 to stop): "))
    head = None
    tail = None

    while value != -1:
        newNode = Node(value)
        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        value = int(input("Enter the value of Node (-1 to stop): "))

    return head


# print length of LL
def LenOfLL(head):
    temp = head
    ans = 0 
    while temp is not None:
        ans += 1
        temp = temp.next

    return ans

#print length of LL recuresively
def LenOfLLRec(head):
    if head is None:
        return 0
    
    return 1 + LenOfLLRec(head.next)


# Insert at head
def insertAtHead(head, value):
    newNode = Node(value)
    newNode.next = head
    head = newNode
    return head

# Insert at tail
def insertAtTail(head, value):
    newNode = Node(value)
    if head is None:
        return newNode
    
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode

    return head

# Insert at tail recursively
def insertAtTailRec(head, value):
    if head is None:
        return Node(value)
    
    smallAns = insertAtTailRec(head.next, value)
    head.next = smallAns
    return head


# delete at index recursively
def deleteAtIndexRec(head, index):
    if head is None or head.next is None:
        return None
    
    if index == 0:
        return head.next
    
    head.next = deleteAtIndexRec(head.next, index - 1)
    return head


# delete an node by value
def deleteByValue(head, value):
    if head is None:
        return None
    
    if head.data == value:
        return head.next
    
    temp = head
    while temp.next is not None and temp.next.data != value:
        temp = temp.next
    
    if temp.next is None:
        print(f"Value {value} not found in the list.")
        return head
    temp.next = temp.next.next
    return head

# delete the node by value recursively
def delByValRec(head, value):
    if head is None or head.next is None:
        return None
    
    if head.data == value:
        return head.next
    
    head.next = delByValRec(head.next, value)
    return head

newhead = take_input()
print_LL(newhead)
print("\nLength of the Linked List is:", LenOfLL(newhead))
print("Length of the Linked List (Recursive):", LenOfLLRec(newhead))
print("\n deleting 10 from the Linked List...")
newhead = delByValRec(newhead, 10)
print_LL(newhead)
print("\ndeletng at index 2...")
newhead = deleteAtIndexRec(newhead, 2)
print_LL(newhead)
print("\nInserting 100 at head...")
newhead = insertAtHead(newhead, 100)
print_LL(newhead)
print("\nLength of the Linked List is:", LenOfLL(newhead))
print("Inserting 200 at tail...")
newhead = insertAtTail(newhead, 200)
print_LL(newhead)
print("\nLength of the Linked List is:", LenOfLL(newhead))
print("Inserting 300 at tail recursively...")
newhead = insertAtTailRec(newhead, 300)
print_LL(newhead)
print("\nLength of the Linked List is:", LenOfLL(newhead))


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def createLLFromList(l1):
    head = None
    tail = None
    for value in l1:
        newNode = Node(value)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

def print_LL(head):
    temp = head
    while temp is not None:
        print(temp.data, end="->")
        temp = temp.next
    print()
    return

def search_by_value_recursive(head, value, index=0):
    if head is None:
        return -1
    if head.data == value:
        return index
    return search_by_value_recursive(head.next, value, index + 1)

# Driver code
newHead = createLLFromList([1, 2, 3, 4, 5])
print("Linked List:")
print_LL(newHead)

value_to_search = 4
print(f"Searching for {value_to_search}...")
index = search_by_value_recursive(newHead, value_to_search)
print(f"Index of {value_to_search} is: {index}")
