#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left)+[root.val]+inorder(root.right)
        numbers = sorted(inorder(root))
        n = len(numbers)
           
        i = 0
        j = n-1
        while i < j:
             if numbers[i] + numbers[j] > k:
                j -= 1
             elif numbers[i] + numbers[j] < k:
                i +=1
             else:
                return True
        return False
solute=Solution()
Tree=TreeNode(3)

Tree.left=TreeNode(2)
Tree.right=Tree()

print(Tree)
