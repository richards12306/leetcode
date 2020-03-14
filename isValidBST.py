# Definition for a binary tree node.
import pdb
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    treeList = []
    def isValidBST(self, root):
        if root == None:
            return True
        
        self.inorderTree(root)

        if self.treeList == sorted(self.treeList):

            return True
        else:
            return False   




    def inorderTree(self,root):
        if root == None:
            return True
        else:
            self.inorderTree(root.left)
            self.treeList.append(root.val)
            self.inorderTree(root.right)
            return True


solute = Solution()
root = TreeNode(0)
print(solute.isValidBST(root))