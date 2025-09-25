class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def generate_predefined_BSTs():
    """
    Returns three root nodes of different BSTs.
    Each BST is larger and structurally different for testing purposes.
    """

    # ---------- BST 1 (Balanced-like structure) ----------
    # Structure:
    #                15
    #         /              \
    #       7                 25
    #     /   \             /    \
    #    3     10         20      30
    #   / \   /  \       /  \    /  \
    #  1   5 8   12    18   22 28   35

    bst1 = TreeNode(15)
    bst1.left = TreeNode(7,
                         TreeNode(3, TreeNode(1), TreeNode(5)),
                         TreeNode(10, TreeNode(8), TreeNode(12)))
    bst1.right = TreeNode(25,
                          TreeNode(20, TreeNode(18), TreeNode(22)),
                          TreeNode(30, TreeNode(28), TreeNode(35)))

    # ---------- BST 2 (Right-skewed but with some left children) ----------
    # Structure:
    # 5 -> 10 -> 15 -> 20 -> 25 -> 30 -> 35
                #   5
                #   \
                #   10
                #  /  \
                # 8    15
                #        \
                #         20
                #        /  \
                #       18   25
                #              \
                #               30
                #                 \
                #                  35

    # with occasional left children

    bst2 = TreeNode(5)
    bst2.right = TreeNode(10)
    bst2.right.left = TreeNode(8)
    bst2.right.right = TreeNode(15)
    bst2.right.right.right = TreeNode(20)
    bst2.right.right.right.left = TreeNode(18)
    bst2.right.right.right.right = TreeNode(25)
    bst2.right.right.right.right.right = TreeNode(30)
    bst2.right.right.right.right.right.right = TreeNode(35)

    # ---------- BST 3 (Complex mixed structure) ----------
    # Structure:
    #                  50
    #          /                 \
    #        30                   70
    #      /   \                /    \
    #    20     40           60       80
    #   /  \   /  \         /  \     /  \
    # 10   25 35  45      55   65  75   90
    #       /                   \        \
    #      22                    68       95

    bst3 = TreeNode(50)
    bst3.left = TreeNode(30,
                         TreeNode(20, TreeNode(10), TreeNode(25, TreeNode(22), None)),
                         TreeNode(40, TreeNode(35), TreeNode(45)))
    bst3.right = TreeNode(70,
                          TreeNode(60, TreeNode(55), TreeNode(65, None, TreeNode(68))),
                          TreeNode(80, TreeNode(75), TreeNode(90, None, TreeNode(95))))

    return bst1, bst2, bst3

def generate_nonBSTs():
    """
    Returns several binary trees that are NOT BSTs (and a couple valid ones) for testing.
    """


    # ---------- Non-BST 1 (Left child > root) ----------
    # 10
    # /
    # 15 (invalid)
    nonbst1 = TreeNode(10)
    nonbst1.left = TreeNode(15)


    # ---------- Non-BST 2 (Right child < root) ----------
    # 20
    # \
    # 5 (invalid)
    nonbst2 = TreeNode(20)
    nonbst2.right = TreeNode(5)


    # ---------- Non-BST 3 (Deep violation) ----------
    # 30
    # / \
    # 15 40
    # / \ / \
    # 5 25 35 50
    # /
    # 45 (invalid — 45 > 30 but in left subtree)
    nonbst3 = TreeNode(30)
    nonbst3.left = TreeNode(15, TreeNode(5), TreeNode(25, TreeNode(45), None))
    nonbst3.right = TreeNode(40, TreeNode(35), TreeNode(50))

        # ---------- Non-BST 4 (Custom invalid tree) ----------
    # 50
    # / \
    # 30 90
    # / \ / \
    # 10 60 80 100
    # (invalid because 60 > 50 but in left subtree)
    nonbst4 = TreeNode(50)
    nonbst4.left = TreeNode(30, TreeNode(10), TreeNode(60))
    nonbst4.right = TreeNode(90, TreeNode(80), TreeNode(100))

    # ---------- Valid BST for comparison ----------
    valid_bst = TreeNode(10, TreeNode(5), TreeNode(20))


    return nonbst1, nonbst2, nonbst3, nonbst4, valid_bst