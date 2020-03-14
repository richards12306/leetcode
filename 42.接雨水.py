#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (48.39%)
# Likes:    840
# Dislikes: 0
# Total Accepted:    51.6K
# Total Submissions: 106.6K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
# 
# 示例:
# 
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# 
#

# @lc code=start
class Solution:
    def trap(self, height):
        if len(height)<3:
            return 0
        maxright=[]
        maxleft=[]
        maxsize=0
        for index in range(len(height)):
            maxsize = max([maxsize,height[index]])
            maxleft.append(maxsize)
        maxsize=0
        for index in range(len(height)-1,-1,-1):
            maxsize = max([maxsize,height[index]])
            maxright.append(maxsize)
        maxright.reverse()
        maxsize=maxright[0]
        result = 0
        for index in range(len(height)-1):
            result = result + min([maxleft[index],maxright[index]]) - height[index]
        return result


# @lc code=end test
height = [5,4,1,2]
solute = Solution()
print(solute.trap(height))
#   #是一个递归饿问题，求最大的两个线中间可以的水量再加上左右暴力计算法
#         if len(height)<3:
#             return 0
#         leftMax,rightMax=0,len(height)-1
#         left,right=0,len(height)-1
#         i=0
#         result = 0
#         while left<=right:
#             leftMax = leftMax if height[leftMax]>height[left] else left
#             rightMax = rightMax if height[rightMax]>height[right] else right
#             left +=1
#             right -= 1
#         if leftMax == rightMax:
#             return self.trap(height[:leftMax+1])+self.trap(height[rightMax:])
#         partHeight = height[leftMax+1:rightMax]
#         for x in partHeight:
#             result = result + x 
#         maxVector = (rightMax - leftMax-1)*min([height[leftMax],height[rightMax]])-result
#         # print("{},{}".format(maxVector,height[leftMax:rightMax+1]))
#         return self.trap(height[:leftMax+1])+self.trap(height[rightMax:])+maxVector