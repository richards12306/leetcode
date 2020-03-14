#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums):
        if len(nums)==1:
            return [nums]
        result = []
        for i in nums:
            currentList = nums.copy()
            currentList.remove(i)
            currentList = self.permute(currentList)
            for sets in currentList:
                result.append([i]+sets) 
                

        return result
            
solute = Solution()
nums = [1,2,3]
# print(solute.permute(nums))    
# @lc code=end

