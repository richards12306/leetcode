#
# @lc app=leetcode.cn id=223 lang=python3
#
# [223] 矩形面积
#

# @lc code=start
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        left = max([A, E])
        right = min([C,G])
        up = min([H, D])
        bottom = max([F, B])
        area = 0
        if right>left and up > bottom:
            area = (right - left) * (up - bottom)
        
        sumarea = (D-B)*(C-A) + (H-F)*(G-E) -area
        return sumarea
# @lc code=end

