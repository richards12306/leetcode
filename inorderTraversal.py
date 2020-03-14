# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def inorderTraversal(self, root):
# recursion method
        # if root != None:
        #     list = self.inorderTraversal(root.left) + [root.val] +  self.inorderTraversal(root.right)
        #     return list
        # else:
        #     return []

#Iteration method
        stack = [[0,root]]
        inorderList=[]
        while stack: 
            tag, node = stack.pop()
            if node is None: 
                continue
            if tag == 0:
                stack.append([0,node.right])
                stack.append([1,node])
                stack.append([([0,node.left])])
            else: 
                inorderList.append(node.val)
                

            





            # if node.left != None and tagNode[0] == 0:
            #     node = node.left
            #     stack.append([0,node])
            # elif node.left == None:
            #     inorderList.append(node.val)

            #     if node.right != None:
            #         node = node.right
            #         stack.append(node)
            #     else:
            #         node = stack[-1]
            #         stack = stack[:-1]
            # return inorderList
                
        
        
        





