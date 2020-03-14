#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        maxlength = 0
        length = 0
        leftborder = 0
        for index in range(len(s)):
            if s[index] not in hashMap:
                hashMap[s[index]] = index
                length += 1
            else:
                maxlength = max(maxlength,length)
                leftborder = max([leftborder,hashMap[s[index]]])
                length = index  - leftborder
                
                hashMap[s[index]] = index
            
        maxlength = max(maxlength,length)    
        return maxlength
# @lc code=end

s="abba"
solute = Solution()
solute.lengthOfLongestSubstring(s)