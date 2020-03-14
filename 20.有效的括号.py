#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0: 
            return False 
        stack = []
    
        for signal in s: 
            if signal in ['(','{','[']: 
                stack.append(signal)
                if len(stack)>len(s)//2+1: 
                    return False
            elif signal in [']',')','}'] and len(stack)==0:
                return False
            elif (signal == ')' and stack[-1] == '(') or (signal ==']' and stack[-1] == '[') or (signal == '}' and stack[-1] == '{'):
                stack.pop() 
            elif signal == ' ': 
                continue
            else: 
                return False
        if len(stack)==0:
                return True
        else: 
            return False
s = "()"
solute = Solution()
solute.isValid(s)   

# @lc code=end

