class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        if root.left and root.right:
            if isBalanced(root.left) and isBalanced(root.right):
                if abs(root.left.height - root.right.height ) <= 1:
                    root.height = max([root.left.height,root.right.height]) + 1
                    return True
        elif not root.left and not root.right:
            root.height = 1
            return True
        elif root.left != None and root.left.height ==1 or root.right !=None and root.right.height == 1:
            root.height =2
            return True
        return False
        

        
        
root = None
if not root:
    root.height = 0


        # stack = [root]
        # height = 0
        # while not stack:
        #     nextStack=[]
        #     for i in stack:
        #         i.height = height
        #         if i.left != None:
        #             nextStack.append(i.left)
        #         if i.right != None:
        #             nextStack.append(i.right)
        #     height +=1
        #     stack = nextStack
