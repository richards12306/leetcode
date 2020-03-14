#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def subcombine(stack, k):
            if k == 0:
                return [[]]
            result = []
            for i in range(len(stack)):
                currentstack = stack.copy()
                currentresult = subcombine(currentstack[i+1:], k - 1)
                
                for sets in currentresult:
                    result.append([currentstack[i]] + sets)
            return result
        stack = []
        for i in range(n):
            stack.append(i + 1)
        return subcombine(stack, k)
        
            
# @lc code=end

