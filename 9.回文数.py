#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse,tmp,pre  = 0,0,x
        if x==0:
            return True
        elif x < 0 or x - x//10*10 == 0: 
            return False
        
        else: 
            while x != 0 and reverse< x: 
                tmp = x - x//10*10
                reverse = reverse*10 +tmp
                # print(tmp,reverse)
                x = x//10
                # print(x,reverse)
        # print(tmp)
        return x == reverse or x == reverse//10
# @lc code=end

