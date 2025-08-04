#implement the queue using list

class QueueUsingList:
    def __init__(self):
        # Initialize an empty list to represent the queue
        self.queue = []

    #enqueue operation
    def enqueue(self, item):
        self.queue.append(item)
        return f"Item {item} added to the queue."
    
    #size operation
    def size(self):
        return len(self.queue)
    
    #front element accessing
    def front(self):
        if self.size() == 0:
            return f"Queue is empty."
        return self.queue[0]
    
    #dequeue operation
    def dequeue(self):
        if self.size() == 0:
            return f"Queue is empty."
        return self.queue.pop(0)
    
    #isEmpty operation
    def is_empty(self): 
        return self.size() == 0
    
# Queue Using Linked lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueUsingLinkedList:
    def __init__(self):
        self.front = None       #out
        self.rear = None        #in
        self.length = 0

    # Enqueue operation
    def enqueue(self, item):
        newNode = Node(item)
        if self.front is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        self.length += 1

    # Size operation
    def size(self):
        return self.length
    
    # Front element accessing
    def get_front(self):
        if self.size() == 0:
            return f"Queue is empty."
        return self.front.data
    
    # is Empty Operation
    def is_empty(self):
        return self.front == None
    
    # Dequeue operation
    def dequeue(self):
        if not self.front:
            return f"Queue is empty."
        removedData = self.front.data
        self.front = self.front.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return removedData


# Example usage
q = QueueUsingLinkedList()
q.enqueue(10)
q.enqueue(20)
print(q.get_front())  # Output: 10
print(q.dequeue())  # Output: 10
print(q.size())  # Output: 1
print(q.is_empty())  # Output: False
print(q.dequeue())  # Output: 20
print(q.is_empty())  # Output: True
print(q.dequeue())  # Output: Queue is empty.
