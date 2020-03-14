#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tag = 1
        result = []
        i = len(digits)-1
        while i >= 0:
            if digits[i]+tag > 9:
                digits[i] = 0
                tag = 1

            else:
                digits[i] = digits[i]+tag
                tag = 0
            result.append(digits[i])
            i -= 1
        if tag == 1:
            result.append(tag)
        result.reverse()
        return result

# @lc code=end
