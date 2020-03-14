#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals):
        intervals.sort()
        result = []
        if len(intervals) == 1:
            return intervals
        index = 0
        while index < len(intervals):
            if index == len(intervals)-1:
                result.append(intervals[index])
                break
            if intervals[index][1] < intervals[index+1][0]:
                result.append(intervals[index])
                index+=1

            else:
                i=1
                maxlength = max([intervals[index][1],intervals[index+i][1]])
                while intervals[index+i][0] <= maxlength:
                    maxlength = max([maxlength,intervals[index+i][1]])
                    i+=1
                    if index+i == len(intervals):
                        break

                result.append([intervals[index][0],maxlength])
                index = index + i 
        return result

# @lc code=end

solute = Solution()
intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
solute.merge(intervals)