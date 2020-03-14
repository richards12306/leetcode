#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits):
        firtstList , secnodeList = [],[]
        result, current = [],[]
        itermdict = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if len(digits) == 0: 
            return []
        
        for index in range(len(digits)): 
            if len(current) == 0: 
                result = []
                # print()
                for letter in itermdict[digits[index]]: 
                    result.append(letter)
                    current = result.copy()
            else: 
                result = []
                for letter in itermdict[digits[index]]:
                    for word in current: 
                        result.append(word+letter)
                current = result.copy()
        return result
solute = Solution()
digits = "23"
solute.letterCombinations(digits)
# @lc code=end

