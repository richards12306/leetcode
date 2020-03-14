class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    depth=0
    def maxDepth(self, root):
        
        if root:
            left_depth, right_depth = self.maxDepth(root.left), self.maxDepth(root.right)
            depth = max([left_depth,right_depth]) + 1
            return depth
        else:
            return 0
root = TreeNode(1)
root.left = TreeNode(3)
root.left.right = TreeNode(3)
root.right = TreeNode(0)

solute = Solution()
print(solute.maxDepth(root))

    