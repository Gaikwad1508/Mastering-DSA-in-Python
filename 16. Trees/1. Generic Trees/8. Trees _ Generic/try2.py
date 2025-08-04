class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        
def print_tree(root):
    if(root == None):
        return
    
    print(f"{root.data}: ", end = '')
    
    for eachChild in root.children:
        print(eachChild.data, end = ', ')
        
    print()
    
    for eachChild in root.children:
        print_tree(eachChild)
            
root = Node(1)
child1 = Node(2)
child2 = Node(3)
child3 = Node(4)
child4 = Node(5)

root.children.append(child1)
root.children.append(child2)
child1.children.append(child3)
child1.children.append(child4)

print_tree(root)