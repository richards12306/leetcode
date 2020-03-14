#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def get_next(p): 
            """ 构造子串needle的匹配表, 以 "ABCDABD" 为例
            i         i          i           i            i             i             i
            ABCDABD  ABCDABD   ABCDABD    ABCDABD     ABCDABD      ABCDABD      ABCDABD
            ABCDABD   ABCDABD    ABCDABD     ABCDABD      ABCDABD      ABCDABD        ABCDABD
            j         j          j           j            j             j             j
            """
            _next = [0] * (len(p)+1) #      A  B  C  D  A  B  D
            _next[0] = -1            # [-1, 0, 0, 0, 0, 1, 2, 0]
            i, j = 0, -1
            while (i < len(p)):
                if (j == -1 or p[i] == p[j]):
                    i += 1
                    j += 1 
                    _next[i] = j
                else:
                    j = _next[j]
            return _next
        
        def kmp(s, p, _next):
            """kmp O(m+n). s以 "BBC ABCDAB ABCDABCDABDE" 为例"""
            i, j = 0, 0
            while (i < len(s) and j < len(p)):
                if (j == -1 or s[i] == p[j]):
                    i += 1
                    j += 1
                else:
                    j = _next[j]
            if j == len(p):
                return i - j
            else:
                return -1
            
        return kmp(haystack, needle, get_next(needle))


        # #这才是真 kmp 啊【cao kmp 好难写】
        # if len(needle)==0 and len(haystack)==0: 
        #     return 0
        # nextList = []
        # j=-1
        # nextList.append(j)
        # for i in range(1,len(haystack)):
        #     j = nextList[i-1]
        #     while haystack[j+1]!=haystack[i] and j>=0: 
        #         j = nextList[j]
        #     if haystack[j+1] == haystack[i]: 
        #         nextList.append(j+1)
        #     else: 
        #         nextList.append(-1)
        

        # j,i = 0,0
        # while j<len(haystack) and i<len(needle):
        #     if haystack[j] == needle[i] or i==-1: 
        #         j+=1
        #         i+=1
        #     else:
        #         i = nextList[i]
        
        # if i==len(needle): 
        #     return j-i
        # else:
        #     return -1


            
# @lc code=end

