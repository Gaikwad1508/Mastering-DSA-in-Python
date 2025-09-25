class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_binary_tree(root):
    #Edge case: if the root is None, return
    if not root:
        return
    
    print(root.data, end = ': ')

    #check if the left child exists
    if root.left:
        print(f'Left -> {root.left.data}', end = ', ')
    else:
        print('Left -> None', end = ', ')

    #check if the right child exists
    if root.right:
        print(f'Right -> {root.right.data}')
    else:
        print('Right -> None')

    print_binary_tree(root.left)
    print_binary_tree(root.right)

# Function to print the binary tree in level order
from collections import deque
def printBinaryTreeLevelWise(root):
    if not root:
        return
    
    queue = deque([root])
    while queue:
        currentNode = queue.popleft()
        print(f"{currentNode.data}: ", end="")
        if currentNode.left:
            print(f"L->{currentNode.left.data}", end = ", ")
            queue.append(currentNode.left)
        else:
            print("L->None", end = ", ")

        if currentNode.right:
            print(f"R->{currentNode.right.data}")
            queue.append(currentNode.right)
        else:
            print("R->None")

# Example usage
from predefinedBT import predefined_binary_tree_inputs

root1, root2, root3 = predefined_binary_tree_inputs()
# print_binary_tree(root1)
# print_binary_tree(root2)

#take input depth-wise
def takeInputBinaryTree():
    data = int(input("Enter the data for the Node: "))

    if data == -1:
        return None
    
    node = BinaryTreeNode(data)
    # Recur for left child
    print(f"Enter the left child of {data}: ", end = '')
    node.left = takeInputBinaryTree()

    # Recur for right child
    print(f"Enter the right child of {data}: ", end = '')
    node.right = takeInputBinaryTree()

    return node

#take input level-wise
from collections import deque
def takeInputBinaryTreeLevelWise():
    data = int(input("Enter the data for the Root: "))
    if data == -1:
        return None
    
    root = BinaryTreeNode(data)
    queue = deque([root])

    while queue:
        currentNode = queue.popleft()

        leftChildData = int(input(f"Enter the left child of {currentNode.data}: "))
        if leftChildData != -1:
            leftChildNode = BinaryTreeNode(leftChildData)
            currentNode.left = leftChildNode
            queue.append(leftChildNode)
        
        rightChildData = int(input(f"Enter the right child of {currentNode.data}: "))
        if rightChildData != -1:
            rightChildNode = BinaryTreeNode(rightChildData)
            currentNode.right = rightChildNode
            queue.append(rightChildNode)

    return root

# print_binary_tree(root1)
printBinaryTreeLevelWise(root2)

# diameter of binary tree
def diameterOfBinaryTree(root):
    if not root:
        return 0
    
    leftHeight = HeightOfBinaryTree(root.left)
    rightHeight = HeightOfBinaryTree(root.right)

    leftDiameter = diameterOfBinaryTree(root.left)
    rightDiameter = diameterOfBinaryTree(root.right)    

    return max(leftDiameter, rightDiameter, leftHeight + rightHeight)


# Height of Binary Tree
def HeightOfBinaryTree(root):
    if not root:
        return 0
    
    leftHeight = HeightOfBinaryTree(root.left)
    rightHeight = HeightOfBinaryTree(root.right)

    return max(leftHeight, rightHeight) + 1


# Optimized diameter of binary tree
def diameterOptimized(root):
    if not root:
        return 0, 0     #height, diameter
        
    leftHeight, leftDiameter = diameterOptimized(root.left)
    rightHeight, rightDiameter = diameterOptimized(root.right)
    
    diameterThroughRoot = leftHeight + rightHeight
    currentHeight = max(leftHeight, rightHeight) + 1
    diameter = max(leftDiameter, rightDiameter, diameterThroughRoot)
    
    return currentHeight, diameter

#construct binary tree from inorder and preorder traversals
def buildTreeFromInorderPreorder(inorder, preorder):
    if not inorder or not preorder:
        return None
    
    rootData = preorder[0]
    root = BinaryTreeNode(rootData)

    rootIndexInInorder = inorder.index(rootData)

    leftInorder = inorder[:rootIndexInInorder]
    rightInorder = inorder[rootIndexInInorder + 1:]

    leftPreorder = preorder[1: 1 + len(leftInorder)]
    rightPreorder = preorder[1 + len(leftInorder):]

    root.left = buildTreeFromInorderPreorder(leftInorder, leftPreorder)
    root.right = buildTreeFromInorderPreorder(rightInorder, rightPreorder)

    return root

def buildTreeFromInorderPreorder2(inorder, preorder, inS, inE, preS, preE):
    if inS > inE or preS > preE:
        return None
    
    rootData = preorder[preS]
    root = BinaryTreeNode(rootData)
    #rootIndexInInorder = inorder.index(rootData)
    rootIndexInInorder = -1
    for i in range(inS, inE + 1):
        if inorder[i] == rootData:
            rootIndexInInorder = i
            break
    
    leftInorderStart = inS
    leftInorderEnd = rootIndexInInorder - 1
    rightInorderStart = rootIndexInInorder + 1
    rightInorderEnd = inE

    leftPreorderStart = preS + 1
    leftPreorderEnd = leftInorderEnd - leftInorderStart + leftPreorderStart
    rightPreorderStart = leftPreorderEnd + 1
    rightPreorderEnd = preE

    root.left = buildTreeFromInorderPreorder2(inorder, preorder, leftInorderStart, leftInorderEnd, leftPreorderStart, leftPreorderEnd)
    root.right = buildTreeFromInorderPreorder2(inorder, preorder, rightInorderStart, rightInorderEnd, rightPreorderStart, rightPreorderEnd) 

    return root

def buildTreeFromInorderPostorder(inorder, postorder, inS, inE, postS, postE):
    if inS > inE or postS > postE:
        return None
    
    rootData = postorder[postE]
    root = BinaryTreeNode(rootData)
    rootIndexInInorder = inorder.index(rootData)

    leftInorderStart = inS
    leftInorderEnd = rootIndexInInorder - 1
    leftPostorderStart = postS
    leftPostorderEnd = leftInorderEnd - leftInorderStart + leftPostorderStart

    rightInorderStart = rootIndexInInorder + 1
    rightInorderEnd = inE
    rightPostorderStart = leftPostorderEnd + 1
    rightPostorderEnd = postE - 1

    root.left = buildTreeFromInorderPostorder(inorder, postorder, leftInorderStart, leftInorderEnd, leftPostorderStart, leftPostorderEnd)
    root.right = buildTreeFromInorderPostorder(inorder, postorder, rightInorderStart, rightInorderEnd, rightPostorderStart, rightPostorderEnd)

    return root


# Example usage of diameterOfBinaryTree
treeDiameter = diameterOptimized(root2)
print(f"Diameter of the tree: {treeDiameter[1]}")
print(f"Height of the tree: {treeDiameter[0]}")

# Example usage of buildTreeFromInorderPreorder
inorder = [4, 2, 5, 1, 6, 3, 7]
preorder = [1, 2, 4, 5, 3, 6, 7]
newRoot = buildTreeFromInorderPreorder2(inorder, preorder, 0, len(inorder) - 1, 0, len(preorder) - 1)
newroot2 = buildTreeFromInorderPostorder(inorder, [4,5,2,6,7,3,1], 0, len(inorder) - 1, 0, len(preorder) - 1)
printBinaryTreeLevelWise(newroot2)
