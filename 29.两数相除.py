#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        tag = 1
        if dividend < 0:
            dividend = -dividend
            tag = tag * -1
        if divisor < 0:
            divisor = -divisor
            tag = -1 * tag
            
        dividend = dividend // divisor * tag
        if dividend > 2147483647 or dividend < -2147483648:
            return 2147483647
        return dividend

# @lc code=end

