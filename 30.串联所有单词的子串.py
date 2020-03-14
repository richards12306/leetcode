#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start


class Solution:
    def findSubstring(self, s, words):
        # 分组考虑，
        nums = len(words)
        wordLength = len(words[0])
        result = []

        for i in range(len(s)):
            index =  
            target = s[index - wordLength: index]
            while index < len(s) and target in currentWords:
                currentWords.remove(s[index - wordLength: index])
                if len(words) == 0:
                    result.append(index - wordLength * nums)
                i += 1

        return result


soulute = Solution()
s = "barfoothefoobarman"
words = ["foo", "bar"]
soulute.findSubstring(s, words)


# @lc code=end
