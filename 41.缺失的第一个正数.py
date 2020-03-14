#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode-cn.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (37.43%)
# Likes:    375
# Dislikes: 0
# Total Accepted:    35.5K
# Total Submissions: 95K
# Testcase Example:  '[1,2,0]'
#
# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
# 
# 示例 1:
# 
# 输入: [1,2,0]
# 输出: 3
# 
# 
# 示例 2:
# 
# 输入: [3,4,-1,1]
# 输出: 2
# 
# 
# 示例 3:
# 
# 输入: [7,8,9,11,12]
# 输出: 1
# 
# 
# 说明:
# 
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
# 
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums):
        # method 1

        # minInt = 1
        # while True:
        #     if minInt not in nums:
        #         return minInt
        #     else:
        #         minInt+=1


        # method 2 缺失整数最大不大于数组长度 length

        length = len(nums)
        # if length == 0:
        #     return 1
        sortList = [0]*(length+1)
        for i in nums:
            if i>0 and i <= length:
                sortList[i-1]=1
        for i in range(length+1):
            if sortList[i] == 0:
                return i+1



        
# @lc code=end

    

solute = Solution()
solute.firstMissingPositive([1])