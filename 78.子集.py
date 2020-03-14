#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return [[]]
        currentsets = self.subsets(nums[1:])
        sets = currentsets.copy()
        for s in currentsets:
            sets.append([nums[0]] + s)
        return sets


# @lc code=end

