#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = []
        num = 1
        stack = []
        result = ""
        for i in range(n):
            stack.append(i+1)
            num = num * (i+1)
            factorial.append(num)
        factorial.reverse()
        factorial = factorial[1:]
        print(factorial,stack)
        for i in range(n - 1):
            # if factorial[i] == 1:
            #     k -= 1
            index = k // factorial[i]
            if k / factorial[i] == k // factorial[i]:
                index = index - 1

            
            k = k % factorial[i]
            result = result + str(stack[index])
            stack.remove(stack[index])
        result = result + str(stack[0])
        return result
            
        
        
        
# @lc code=end

