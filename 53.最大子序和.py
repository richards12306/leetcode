#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums):
       
        #分治
        #分别计算中心元素左右两边的最大值，再单独计算包含中心元素的子数组最大值
        if len(nums)==1:
            return nums[0]
        else:
            leftNum = nums[:len(nums)//2]
            rightNum = nums[len(nums)//2:]
            maxLeft = self.maxSubArray(leftNum)
            maxRight = self.maxSubArray(rightNum)

            maxL = leftNum[-1]
            tmp=0
            for index in range(len(leftNum)-1,-1,-1):
                tmp += leftNum[index]

                maxL = max([maxL,tmp])
            maxR = rightNum[0]
            tmp=0
            for index in range(len(rightNum)):

                tmp += rightNum[index]
                maxR = max([maxR,tmp])
            
            return max([maxLeft,maxRight,maxR+maxL])
            




              
        
# @lc code=end

nums = [-2,1,-3,4,-1,2,1,-5,4]
solute = Solution()
solute.maxSubArray(nums)
 # 贪心算法
        # currentSum = maxSum = nums[0]
        # for i in range(1,len(nums)):
        #     currentSum = max([currentSum+nums[i],nums[i]])
        #     maxSum = max(maxSum,currentSum)
        # return maxSum

        #DP
        # maxSum = 0
        # length = len(nums)
        # for i in range(1,length,1):
        #     if nums[i-1]>0:
        #         nums[i] = nums[i] += nums[i-1]
        #     maxSum = max([nums[i],maxSum])
        # return maxSum
