# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if root :
            if self.isEqual(root.left,root.right):
                return True
            else: 
                return False    
        else:
            return True


    def isEqual(self,left,right):
      
        if left and right:
            if left.val == right.val:
                return self.isEqual(right.left,left.right) and self.isEqual(left.left,right.right)

        elif not left and not right:
            return True
        else:
            return False

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
solute = Solution()
print(solute.isSymmetric(tree))