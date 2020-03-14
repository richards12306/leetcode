#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs):
        #当然可以用分治，讨论左右的最长前缀
       
    
# @lc code=end


strs = ["flower","flow","flight"]
solute = Solution()
solute.longestCommonPrefix(strs)


#最简单的横向遍历
    # if len(strs) == 0: 
        #     return ""
        # index = 0
        # current = 0

        # s=""
        # while index < len(strs[0]): 
        #     current = strs[0][index]
        #     for word in strs: 

        #         if index >= len(word) or  word[index] != current:
        #             return s
        #     s = s + current
        #     index +=1
        # return s


        #分治
         # if len(strs) == 1:
        #     return strs[0]
        # if len(strs) == 0: 
        #     return ""
        
        # else:
        #     leftPrefix = self.longestCommonPrefix(strs[:len(strs)//2])
        #     rightPrefix = self.longestCommonPrefix(strs[len(strs)//2:])

        #     index = 0
        #     s = ""
        #     while index < len(leftPrefix) and index < len(rightPrefix) and leftPrefix[index]==rightPrefix[index]:
        #         # print(rightPrefix[index])
        #         s = s+rightPrefix[index]
        #         index+=1

                    
        #     return s