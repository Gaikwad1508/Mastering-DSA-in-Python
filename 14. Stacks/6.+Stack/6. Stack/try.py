class StackUsingList:
    def __init__(self):
        self.__stack = []    

    def push(self, item):
        """Push an item onto the stack."""
        self.__stack.append(item)

    def isEmpty(self):
        if len(self.__stack) == 0:
            return True
        return False
    
    def size(self):
        return len(self.__stack)
    
    def top(self):
        if self.isEmpty():
            return None
        return self.__stack[-1]
    def pop(self):
        if self.isEmpty():
            return None
        return self.__stack.pop()
    
# Stack Implementation using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackUsingLL:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        return f"Item {item} pushed onto the stack."
    
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        return self.length
    
    def top(self):
        if self.isEmpty():
            return None
        return self.head.data
    
    def pop(self):
        if self.isEmpty():
            return f"Stack is empty, cannot pop."
        poppedItem = self.head.data
        self.head = self.head.next
        self.length -= 1
        return poppedItem


    


# Example usage
myStack = StackUsingLL()
print(myStack.isEmpty())  # True
myStack.push(10)
myStack.push(20)
myStack.push(30)
myStack.push(40)
print(myStack.isEmpty())  # False
print(myStack.pop())  # 40
print(myStack.pop())  # 30
print(myStack.size())  # 2
print(myStack.top())  # 20
print(myStack.pop())  # 20
print(myStack.pop())  # 10
print(myStack.pop())  # None (stack is empty)