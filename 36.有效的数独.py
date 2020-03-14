#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def subMatrixIsValid(martix):
            stack = []
            for i in martix:
                if i != '.' and i not in stack:
                    stack.append(i)
                elif i in stack:
                    return False
            return True
        tag = True
        for column in board:
            tag = tag and subMatrixIsValid(column)
        print(tag)
        for i in range(9):
            row = []
            for j in range(9):
                row.append(board[j][i])
            tag = tag and subMatrixIsValid(row)
        print(tag)
        submatrix = []
        for i in range(3):
            for j in range(3):
                submatrix = []
                for a in range(3):
                    for b in range(3):
                        submatrix.append(board[i * 3 + a][j * 3 + b])
                tag = tag and subMatrixIsValid(submatrix)
        print(tag)
        return tag


# @lc code=end
