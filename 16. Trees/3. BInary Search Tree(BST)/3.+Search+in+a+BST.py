from predefinedBSTs import generate_predefined_BSTs, generate_nonBSTs
from commons import BSTNode, print_binary_tree, print_bst

root1,root2,root3 = generate_predefined_BSTs()


def search_in_BST(root,value):
    if not root:
        return False
    
    if root.data == value:
        return True
    
    elif value < root.data:
        return search_in_BST(root.left, value)
    
    else:
        return search_in_BST(root.right, value)
    
# Example usage:
found = search_in_BST(root2, 18)
print("Found 18 in BST2:", found)  # Output: True