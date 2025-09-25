from predefinedBSTs import generate_predefined_BSTs, generate_nonBSTs
from commons import print_binary_tree, print_bst
nonbst1, nonbst2, nonbst3, nonbst4, valid_bst = generate_nonBSTs()
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_max(node):
    if(node is None):
        return float("-inf")
    
    left_max = find_max(node.left)
    right_max = find_max(node.right)

    ans = max(left_max,right_max,node.data)
    return ans

def find_min(node):
    if(node is None):
        return float("inf")

    left_min = find_min(node.left)
    right_min = find_min(node.right)

    ans = min(left_min,right_min,node.data)
    return ans
    

def checkBST(root):
    if(root is None):
        return True # Base condition : Empty Tree is a BST
    
    left_max = find_max(root.left)
    right_min = find_min(root.right)

    left_BST = checkBST(root.left)
    right_BST = checkBST(root.right)

    ans = left_BST and right_BST and (left_max < root.data) and (root.data < right_min)

    return ans

def checkBST_Better(root):
    if not root:
        return True, float('inf'), float('-inf')
    
    is_left_bst, left_min, left_max = checkBST_Better(root.left)
    is_right_bst, right_min, right_max = checkBST_Better(root.right)

    if (is_left_bst and is_right_bst and left_max < root.data < right_min):
        return True, min(left_min, root.data), max(right_max, root.data)
    else:
        return False, min(left_min, root.data), max(right_max, root.data)



def checkBST_limit(root,minimum,maximum):
    if(root is None):
        return True

    if(root.data < minimum or root.data > maximum):
        return False
    
    ansLeft = checkBST_limit(root.left,minimum,root.data-1)
    ansRight = checkBST_limit(root.right,root.data+1,maximum)

    return ansLeft and ansRight


nonbst1, nonbst2, nonbst3, nonbst4, valid_bst = generate_nonBSTs()
print(checkBST_limit(nonbst4,float('-inf'),float('inf')))

root1,root2,root3 = generate_predefined_BSTs()
print(checkBST_limit(root3,float('-inf'),float('inf')))

root4 = BSTNode(5)
root4.left = BSTNode(10)
root4.right = BSTNode(15)

print(checkBST_limit(root4,float('-inf'),float('inf')))