#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s):
#中心扩展算法 一个 长度为 n 的字符串有 2n - 1 个中心 aabcd 【aa 以中间的间隙为中心】
 # 特判
        size = len(s)
        if size < 2:
            return s

        # 得到预处理字符串
        t = "#"
        for i in range(size):
            t += s[i]
            t += "#"
        # 新字符串的长度
        t_len = 2 * size + 1
        # 当前遍历的中心最大扩散步数，其值等于原始字符串的最长回文子串的长度
        max_len = 1
        # 原始字符串的最长回文子串的起始位置，与 max_len 必须同时更新
        start = 0

        for i in range(t_len):
            cur_len = self.__center_spread(t, i)
            if cur_len > max_len:
                max_len = cur_len
                start = (i - max_len) // 2
        return s[start: start + max_len]

    def __center_spread(self, s, center):
        size = len(s)
        i = center - 1
        j = center + 1
        step = 0
        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
            step += 1
        return step

        # if len(s)==0:
        #     return ""
        # maxlength, length = 0, 0 
        # maxindex = 0
        # begin = end = 0

        # for index in range(2*(len(s)-1)):
        #     if index%2==0:
        #         length = 1
        #         lindex = rindex = index//2
        #     else:
        #         length = 2
        #         lindex = index//2
        #         rindex = lindex + 1
        #     # print(s[lindex],s[rindex])




        #     for i in range(len(s)):
        #         lindex = lindex-i
        #         rindex = rindex+i
        #         if lindex>=0 and rindex<=len(s)-1:
        #             if s[lindex] == s[rindex]:
        #                 length = length +2*i 

        #             else:
                       
        #                 break                   
        #         else:  
        #             lindex+=1
        #             rindex-=1
        #             break 
        #     if length>maxlength:
        #         begin = lindex
        #         end = begin+length

        #         maxlength = length

       

        # return s[begin:end]

solute = Solution()
s="babad"
solute.longestPalindrome(s)


        

# @lc code=end

                
  # for index in range(len(s)+1):
        #     length = 0
        #     lindex = index//2
        #     rindex = lindex + 1
        #     for i in range(len(s)):
        #         lindex = index-i
        #         rindex = index+i
        #         if lindex>=0 and rindex<=0:
        #             length = length +2*i 
        #         else: 
        #             break
        #     if length>maxlength:
        #         begin = index - (length-1)/2
        #         num = []
        #         for i in range(length):
        #             num.append(s[begin+i])
        #         maxlength = length               

