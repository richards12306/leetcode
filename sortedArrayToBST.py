class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
        if len(nums) ==  0:
    def sortedArrayToBST(self, nums):
            return None
        begin, end = 0, len(nums)-1
        index = (begin + end + 1)/2
        tree = TreeNode(nums[index])
        tree.left = self.sortedArrayToBST(nums[:index])
        tree.right = self.sortedArrayToBST(nums[index+1:])
        return tree
        

