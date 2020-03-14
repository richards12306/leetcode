#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates, target):
        ListResult = []
        listSets = []
        candidates.sort()
        for i in range(len(candidates)):

            if candidates[i] > target or i>0 and candidates[i-1]==candidates[i]:
                continue
            List = candidates[i+1:]
            
            if candidates[i] == target:
                ListResult.append([candidates[i]])
            if candidates[i] < target:
                listSets = self.combinationSum2(List,target-candidates[i])
                if not listSets:
                    continue
                for sets in listSets:
                    ListResult.append([candidates[i]]+sets)
        return ListResult
     
# @lc code=end
def combinationSum2(self, candidates, target):
        candidates.sort()####
        def backtrack(candidates, target,  start, list_one):
            sum_list=sum(list_one)
            if sum_list==target:  #and list_one not in res_list :
                res_list.append(list_one[:])
            else:
                for i in range(start, end):
                    if sum_list  > target : break    ######剪枝
                    if i > start and candidates[i] == candidates[i-1]:continue  ####此处避免重复值
                    list_one.append(candidates[i])
                    backtrack(candidates, target, i+1, list_one)
                    list_one.pop()
        res_list = []
        list_one = [] 
        end=len(candidates)       
        backtrack(candidates, target, 0, list_one)
        return res_list


solute = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
solute.combinationSum2(candidates,target)