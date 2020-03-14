# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        def generate_trees(start, end):
            if start > end:
                return [None,]
            
            all_trees = []
            for i in range(start, end + 1):  # pick up a root
                # all possible left subtrees if i is choosen to be a root
                left_trees = generate_trees(start, i - 1)
                
                # all possible right subtrees if i is choosen to be a root
                right_trees = generate_trees(i + 1, end)
                
                # connect left and right subtrees to the root i
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            
            return all_trees
        
        return generate_trees(1, n) if n else []


    #     nums = [i for i in range(1,n+1)]
    #     print(nums)
    #     return self.listGenerateTrees(nums)


    # def listGenerateTrees(self,nums):
    #     if len(nums) == 0:
    #         return [[]]
    #     else:
    #         for i in range(len(nums)):
    #             root = TreeNode(nums[i])
    #             leftTreeList = self.listGenerateTrees(nums[:i])
    #             rightTreeList = self.listGenerateTrees(nums[i+1:])


            
    #             for i in range(len(leftTreeList)):
    #                 for j in range(len(rightTreeList)):
    #                     root.left = leftTreeList[j]
    #                     root.right = rightTreeList[i]
    #                     treeList.append(root)
    #     return treeList


solute = Solution()
print(solute.generateTrees(3))

