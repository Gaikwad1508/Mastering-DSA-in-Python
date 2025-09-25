from predefinedBSTs import generate_predefined_BSTs, generate_nonBSTs
from commons import BSTNode, print_binary_tree, print_bst

root1,root2,root3 = generate_predefined_BSTs()
nonbst1, nonbst2, nonbst3, nonbst4, valid_bst = generate_nonBSTs()

# Convert sorted list to balanced BST
def lstToBst(lst):
    if not lst:
        return None

    mid = len(lst)//2
    node = BSTNode(lst[mid])

    node.left = lstToBst(lst[:mid])
    node.right = lstToBst(lst[mid+1:])

    return node

#check is Bst (Wrong approach)
def isBST(root):
    if not root:
        return True
    
    if root.left and root.left.data > root.data:
        return False
    
    if root.right and root.right.data < root.data:
        return False
    
    return isBST(root.left) and isBST(root.right)

#Check is Bst (Correct approach)
def find_max(root):
    if not root:
        return float("-inf")
    
    max_left = find_max(root.left)
    max_right = find_max(root.right)

    return max(root.data, max_left, max_right)

def find_min(root):
    if not root:
        return float("inf")
    
    min_left = find_min(root.left)
    min_right = find_min(root.right)

    return min(root.data, min_left, min_right)

def isBSTCorrected(root):
    if not root:
        return True
    
    left_max = find_max(root.left)
    right_min = find_min(root.right)

    ans = left_max < root.data < right_min and isBSTCorrected(root.left) and isBSTCorrected(root.right)
    return ans

def printInRange(root, low, high):
    if not root:
        return
    
    if low < root.data:
        # Go to left subtree
        printInRange(root.left, low, high)

    if low <= root.data <= high:
        print(root.data, end=' ')

    if high > root.data:
        # Go to right subtree
        printInRange(root.right, low, high)

def checkBstLimit(root, minimum = float("-inf"), maximum = float("inf")):
    if not root:
        return True
    
    if root.data < minimum or root.data > maximum:
        return False
    
    leftAns = checkBstLimit(root.left, minimum, root.data-1)
    rightAns = checkBstLimit(root.right, root.data+1, maximum)

    return leftAns and rightAns

#######     Creating BST Class    ########
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None


    def insertHelper(self, data, root):
        if not root:
            root = BSTNode(data)
            return root

        if data < root.data:
            root.left = self.insertHelper(data, root.left)

        else:
            root.right = self.insertHelper(data, root.right)
        
        return root
        
    def insert(self, data):
        self.root = self.insertHelper(data, self.root)


    def searchHelper(self, data, root):
        if not root:
            return False
        
        if root.data == data:
            return True
        
        if data < root.data:
            return self.searchHelper(data, root.left)
        
        else:
            return self.searchHelper(data, root.right)
        

    def search(self, data):
        return self.searchHelper(data, self.root)
    
    def get_max_node(self, root):
        current = root
        while current.right:
            current = current.right
        return current

    def deleteHelper(self, data, root):
        if not root:
            return None
        
        if data < root.data:
            root.left = self.deleteHelper(data, root.left)

        elif data > root.data:
            root.right = self.deleteHelper(data, root.right)
        
        #We are now on that node which is to be deleted
        else:   

            #if left subtree is absent
            if not root.left:
                return root.right
            
            #if right subtree is absent
            elif not root.right:
                return root.left
            
            #When both subtrees present
            else:
                max_smaller_node = self.get_max_node(root.left)
                root.data = max_smaller_node.data
                root.left = self.deleteHelper(max_smaller_node.data, root.left)

        return root

    def delete(self, data):
        return self.deleteHelper(data, self.root)


classObject = BST()
classObject.insert(10)
classObject.insert(20)
classObject.insert(30)
classObject.insert(5)
classObject.insert(25)

root = classObject.root
classObject.delete(10)
print_binary_tree(root)

# print(classObject.search(5))

# # Example usage
# sorted_list = [1, 2, 3, 4, 5, 6, 7]
# balanced_bst = lstToBst(sorted_list)   
# print_bst(balanced_bst)
# print()
# print_binary_tree(balanced_bst)

# print("Is BST:", isBST(root1))
# print("Is BST:", isBST(nonbst4))  # Should be False
# print("Is BST Corrected:", isBSTCorrected(root1))
# print("Is BST Corrected:", isBSTCorrected(nonbst4))  # Should be False
# print("Is BST Corrected with limits:", checkBstLimit(root1))
# print("Is BST Corrected with limits:", checkBstLimit(nonbst4))  # Should be False

# print_binary_tree(root1)
# print("Is BST:", isBST(root1))
# print("Elements in range [19, 25]:", end=' ')
# printInRange(root1, 19, 25)