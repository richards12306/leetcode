#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [0 for i in range(len(s))]
        maxlength = 0
        length = 0

        for i in range(1, len(s)):
            if s[i - 1] == '(' and s[i] == ')':
                dp[i] = dp[i-2]+2
            if s[i - 1] == ')' and s[i] == ')':
                if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i-dp[i-1]-2]

        return max(dp)
#         stack = []
#         length, maxlength = 0, 0

#         for i in range(len(s)):
#             if s[i] == '(':
#                 stack.append(i)
#             elif s[i] == ')' and len(stack) > 0:
#                 left = stack.pop()
#                 length = max([length, i - left+1])
#         return length


# solute = Solution()
# s = ")()())"
# solute.longestValidParentheses(s)


# @lc code=end
# 动态规划
