#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums):
        maxlength=0
        if len(nums) == 1:
            return True
        for index in range(len(nums)):
            if (index==maxlength and nums[index]==0):
                return False
            else:
                if index + nums[index] > maxlength:
                    maxlength = index + nums[index]
                    if maxlength>=len(nums)-1:
                        return True
            

        
# @lc code=end

nums=[2,3,1,1,4]
solute = Solution()
print(solute.canJump(nums))