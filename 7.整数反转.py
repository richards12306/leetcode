#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        tag = 1
        if x <= -2**31 or x >= 2**31-1:
            return 0
        elif x<0: 
            tag = -1
            x = x * tag
        tmp = 0
        while x!= 0: 
            pop = x-(x//10*10)
            x = x//10
            tmp = tmp*10+pop
        # print(result
        if tmp <= -2**31 or tmp >= 2**31-1:
            return 0
        return tmp*tag
                

# @lc code=end

