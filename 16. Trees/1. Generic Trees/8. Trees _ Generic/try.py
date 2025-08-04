class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

root = Node(1)
child1 = Node(2)
child2 = Node(3)
child3 = Node(4)

root.children.append(child1)
root.children.append(child2)
root.children.append(child3)

def print_tree_detailed(root):
    if root is None:  # Edge Case
        return 
    
    print(f"{root.data}: ", end = '')

    for child in root.children:
        print(child.data, end=',')

    print()
    
    for child in root.children:
        print_tree_detailed(child)


def take_input():
    data = int(input("Enter the data for the Node: "))
    node = Node(data)

    num_children = int(input(f"Enter the number of Children for {data}: "))

    for _ in range(num_children):
        child = take_input()
        node.children.append(child)

    return node

from collections import deque
def take_input_level_wise():
    root_data = int(input("Enter the data for the root node: "))
    root = Node(root_data)
    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        num_children = int(input(f"Enter the number of children for {current_node.data}: "))
        for i in range(num_children):
            child_data = int(input(f"Enter the data for the {i + 1} child node: "))
            child_node = Node(child_data)
            current_node.children.append(child_node)
            queue.append(child_node)
    return root

def num_of_nodes(root):
    if not root:
        return 0
    
    count = 1

    for child in root.children:
        count += num_of_nodes(child)

    return count

def height_of_tree(root):
    if not root:
        return 0
    
    height = 1
    max_child_height = 0

    for child in root.children:
        max_child_height = max(max_child_height, height_of_tree(child))
    
    height += max_child_height
    return height

def preorder_traversal(root):
    if not root:
        return
    
    print(root.data, end = ' ')

    for child in root.children:
        preorder_traversal(child)

def postorder_traversal(root):
    if not root:
        return
    
    for child in root.children:
        postorder_traversal(child)

    print(root.data, end = ' ')


from genericTreesInput import predefined_generic_tree_inputs
root1, root2, root3 = predefined_generic_tree_inputs()

print(num_of_nodes(root1))  # Output: 5
print(num_of_nodes(root2))  # Output: 6
print(num_of_nodes(root3))  # Output: 5

postorder_traversal(root1)  # Output: 4 5 2 3 1
print()
postorder_traversal(root2)  # Output: 20 50 60 30 40 10
print()
postorder_traversal(root3)  # Output: 400 500 200 300 100