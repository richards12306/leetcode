# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        levelTraversal = []
        thisLevelQueue=[]
        nextLevelQueue=[]
        if root == None:
            return []
        else:
            thisLevelQueue.append(root)
        while len(thisLevelQueue)>0:
            level = []
            nextLevelQueue=[]
            for node in thisLevelQueue:
                # if node!=None:
                if node.left !=None:
                    nextLevelQueue.append(node.left)
                if node.right !=None:
                    nextLevelQueue.append(node.right)
                level.append(node.val)
            levelTraversal.append(level)
            thisLevelQueue = nextLevelQueue
        levelTraversal.reverse()
        return levelTraversal
solute = Solution()
root = TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
node = root.right
node.right = TreeNode(7)
node.left = TreeNode(15)
print(solute.levelOrderBottom(root))





                
                
        