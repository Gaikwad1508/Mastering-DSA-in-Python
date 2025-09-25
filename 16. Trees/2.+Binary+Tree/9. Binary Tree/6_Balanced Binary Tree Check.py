def print_binary_tree(root):
    if(root is None):  # Base Case
        return

    # Format : Node : L->LeftChildData , R->RightChild Data
    print(root.data, end=": ")

    if(root.left is not None):
        print(f"L->{root.left.data}",end = ", ")
    else:
        print("L->None",end=",")

    if(root.right is not None):
        print(f"R->{root.right.data}")
    else:
        print("R->None")
 
    # Recur for the left and right children
    print_binary_tree(root.left)
    print_binary_tree(root.right)


#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def height(self, root):
        if not root:
            return 0
        
        h = 1 + max(self.height(root.left), self.height(root.right))
        return h

    def isBalanced(self, root):
        if not root:
            return True
        
        if (self.height(root.left) - self.height(root.right)) not in [1, 0, -1]:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
            


from predefinedBT import predefined_binary_tree_inputs
root1, root2, root3 = predefined_binary_tree_inputs()

#example for not balanced tree
root1.left.left.left = TreeNode(7)  # Making the tree unbalanced
root1.left.left.left.left = TreeNode(8)  # Further unbalancing the tree

Sol = Solution()
print(Sol.isBalanced(root1))

        