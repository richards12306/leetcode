# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p,q):
        if p and q:
            if p.val != q.val:
                return False
            else: 
                return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        elif not p and not q:
            return True
        else:
            return False


                
                


    #     stack=[]
    #     list_q, list_p=[], []
    #     self.printTree(q,stack,list_q)
    #     self.printTree(p,stack,list_p)
    #     if len(list_p) != len(list_q):
    #         return False
    #     else:
    #         for i in range(len(list_q)):
    #             if list_q[i] != list_p[i]:
    #                 return False
    #         return True

    
    # def printTree(self,tree,stack,mid_list):
    #     if tree == None:
    #         return mid_list
    #     if tree.left == None and tree.right == None:
    #         mid_list.append(tree.val)
    #         if len(stack) > 0:
    #             tree = stack[-1]

    #         return mid_list


    #     stack.append(tree)
    #     mid_list.append(tree.val)
    #     if tree.left != None:
    #         self.printTree(tree.left,stack,mid_list)
    #     if tree.right != None:
    #         self.printTree(tree.right,stack,mid_list)
        
        

                





solute = Solution()
tree = TreeNode(2)
tree.left = TreeNode(1)
tree.right = TreeNode(3)
stack=[]
mid_list=[]
solute.printTree(tree,stack,mid_list)
print(mid_list)

    