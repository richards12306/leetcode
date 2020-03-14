#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m=len(obstacleGrid[0])
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j]==1:
                    row,coloumn = i+1,j+1
                    allResult = self.uniquePaths(n,n)
                    lostResult = self.uniquePaths(row,coloumn) * self.uniquePaths(n-row+1,n-coloumn+1)
                    return allResult-lostResult
        return self.uniquePaths(n,m)
    def uniquePaths(self, m, n):
        m,n = m-1,n-1
        result=1
        frac=1
        for i in range(m+n,n,-1):
            result = result*i
        for i in range(1,m+1):
            frac = frac * i
        if m==0 or n==0:
            return 1
        return int(result/frac)
# @lc code=end
solute = Solution()
matrix = [[0]]
solute.uniquePathsWithObstacles(matrix)
