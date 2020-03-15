#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for coloumn in range(len(board[0])):
                if board[row][coloum] == word[0]:
                    stack.append([row,coloumn])

# @lc code=end

