#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s, numRows):
        #一个 z 需要 3n-2个元素

        if numRows==1 or numRows>=len(s) :return s
        r,j,k=['']*numRows,0,1
        for i in s:
            r[j]+=i
            j+=k
            if j==0 or j==numRows-1 : k=-k
        print(r)
        return "".join(r)
        
solute = Solution()
s = "PAYPALISHIRING"
solute.convert(s,3)
# @lc code=end

