#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums):
         #一步最远到哪里，第二次再计算
        maxLength = 0
        leftBorder = 0
        rightBorder = 1
        if len(nums) == 1:
            return 0
        tag = 0
        while True:
            for index in range(leftBorder,rightBorder,1): 
                if rightBorder <nums[index]+index+1:
                    maxLength = index
                    rightBorder = nums[maxLength]+maxLength+1
            leftBorder = maxLength+1
            tag+=1
            if rightBorder >= len(nums):
                return tag
        return tag



            # for index in (maxLength-leftBorder):
            #     rangeList.append(leftBorder+index)
        
# @lc code=end
solute = Solution()
nums = [1,2,3]
print(solute.jump(nums))
