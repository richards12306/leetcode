#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix):
        columns = len(matrix)
        rows = len(matrix[0])
        for column in range(columns):
            for row in range(column,rows):
                matrix[column][row], matrix[row][column] = matrix[row][column], matrix[column][row]
        for column in range(columns):
            for index in range((rows+1)//2):
                matrix[column][index], matrix[column][rows - index-1] = matrix[column][rows - index-1], matrix[column][index]
    
        """
        Do not return anything, modify matrix in-place instead.
        """
        
# @lc code=end

matrix = [[1,2,3],[4,5,6],[7,8,9]]
solute = Solution()
print(solute.rotate(matrix))