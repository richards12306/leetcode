#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#

# @lc code=start

#读题目很累，希望可以有一个简单的题目版本
#需要得出最长的仅由两个元素组成的序列
#最简单的方法是遍历，
class Solution:
    def totalFruit(self, tree):
        element1,element2 = tree[0],tree[0]
        prelength = 0
        length = 0
        maxlength = 0
        for iterm in tree:
            if iterm == element1:
                prelength += 1
                length += 1
                continue

            elif iterm == element2:
                element1,element2 = element2,element1
                prelength = 1
                length += 1
                continue
            
            else:
                maxlength = max(maxlength,length)
                element2, element1 = element1, iterm
                length = prelength +1
                prelength = 1
                continue     
        maxlength = max(maxlength,length)
        return maxlength
        
# @lc code=end

tree = [3,3,3,1,2,1,1,2,3,3,4]
solute = Solution()
print(solute.totalFruit(tree))