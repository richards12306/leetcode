#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums):

        nums.sort()
        
        def permute(nums):
            result = []
            if len(nums) == 1:
                return [nums]
            i = 0
            while i <= len(nums) - 1:
                currentNums = nums.copy()
                currentNums.remove(nums[i])
                currentresult = permute(currentNums)
                constanresult = []
                for sets in currentresult:
                    t= [nums[i]] + sets
                    result.append(t)
                i+=1
                while i > 0 and i <= len(nums)-1 and nums[i - 1] == nums[i]:
                    i += 1
                
            return result

        return permute(nums)
solute = Solution()
nums = [1, 1, 2]
solute.permuteUnique(nums)
                
# @lc code=end

# def dfs(nums, size, depth, path, used, res):
        #     if depth == size:
        #         res.append(path.copy())
        #         return
        #     for i in range(size):
        #         if not used[i]:

        #             if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
        #                 continue

        #             used[i] = True
        #             path.append(nums[i])
        #             dfs(nums, size, depth + 1, path, used, res)
        #             used[i] = False
        #             path.pop()

        # size = len(nums)
        # if size == 0:
        #     return []

        # nums.sort()

        # used = [False] * len(nums)
        # res = []
        # dfs(nums, size, 0, [], used, res)
        # return res
