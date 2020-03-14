#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (68.19%)
# Likes:    518
# Dislikes: 0
# Total Accepted:    61.1K
# Total Submissions: 89.6K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的数字可以无限制重复被选取。
# 
# 说明：
# 
# 
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates, target):
        ListResult = []
        listSets = []
        for i in candidates:
            if i > target:
                continue
            index = candidates.index(i)
            List = candidates[index:]
            
            if i == target:
                ListResult.append([i])
            if i < target:
                listSets = self.combinationSum(List,target-i)
                if not listSets:
                    continue
                for sets in listSets:
                    ListResult.append([i]+sets)
        return ListResult

        
# @lc code=end
candidates = [2,3,6,7]
target = 7
solute = Solution()
print(solute.combinationSum(candidates,target))

