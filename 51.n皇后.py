#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n):
        
        def backtrap(row,matrix):
            currentMatrix = matrix.copy()
            for coloum in range(n):
                if matrix[row][coloum] == 0:
                    matrix[row][coloum] = 1
                    for i in range(row, n):
                        matrix[i][coloum] = 1
                    i,j = row,coloum
                    while i < n and j >= 0:
                        matrix[i + 1][j - 1] = 1
                    i, j = row, coloum
                    while i < n and j < n:
                        matrix[i + 1][j + 1] = 1
                    for i in range(n):
                        matrix[row][i] = '.'
                    matrix[row][coloum] = 'Q'
                    if row == n - 1:
                        result.append(matrix)
                        return
                    else:
                        backtrap(row + 1,matrix)
                    matrix = currentMatrix.copy
        matrix = []
        for i in range(n):
            matrix.append([0] * n)
        result = []
        print(matrix)
        print('asdfasfasfasd')
        backtrap(0,matrix)
        return result
solute = Solution()
n=4
solute.solveNQueens(n)        
        
# @lc code=end

