#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix):
        rows = len(matrix)
        if rows ==0:
            return []
        columns = len(matrix[0])
        result = []
        column, row = 0,0
        while True:
            if columns >0:
                for column in range(column,column+columns,1):
                    result.append(matrix[row][column])
                rows-=1
            else:
                return result

            if rows > 0 :
                for row in range(row+1,row+1+rows,1):
                    result.append(matrix[row][column])
                columns-=1
            else:
                return result

            if columns>0:
                for column in range(column-1,column-columns-1,-1):
                    result.append(matrix[row][column])
                rows-=1
            else:
                return result

            if rows >0:
                for row in range(row-1,row-rows-1,-1):
                    result.append(matrix[row][column])
                columns-=1
                column+=1
            else:
                return result

        return result

        
# @lc code=end

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
solute = Solution()
print(solute.spiralOrder(matrix))