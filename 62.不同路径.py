#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m, n):
        m,n = m-1,n-1
        result=1
        frac=1
        for i in range(m+n,n,-1):
            result = result*i
        for i in range(1,m+1):
            frac = frac * i
        # print(frac,result)
        # print(matrix[1:100])
        # print(matrix[100:200])
        if m==0 or n==0:
            return 1
        return int(result/frac)
        
        
# @lc code=end

solute = Solution()
solute.uniquePaths(100,3)