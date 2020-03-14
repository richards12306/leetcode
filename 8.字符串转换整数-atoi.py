#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
#coding:utf-8
class Solution:
    def myAtoi(self, str):
        #难度不高，但是对于我这种写代码很憨批的老是犯低级错误的人 emmm
        #开始考虑每个代码写注释了

        #处理string，去除最前面的所有空格
        return max(min(int(*re.findall(('^[\+\-]?\d+',str.lstrip()))),2**31-1),-2**31)
        # tag,tmp,i = 1,0,1
        # str = str.strip()

        # firstLegalElement = ['+','-','1','2','3','4','5','6','7','8','9','0']
        # legalElement = ['1','2','3','4','5','6','7','8','9','0']
        # #判断第一位是不是合法的字符，并得出符号位
        # if str[0] not in firstLegalElement: 
        #     return 0
        # elif str[0] == '-': 
        #     tag = -1
        # elif str[0] == '+': 
        #     tag = 1
        #     #第一位就是数字
        # else: 
        #     i = 0
        
        # #遍历字符串得出并转数字

        # while i<len(str): 
        #     if str[i] in legalElement: 
        #         tmp = tmp*10 + int(str[i])
        #         i+=1
        #     else: 
        #         break

        # if tag == 1 and tmp > 2**31-1: 
        #     return 'INT_MAX (231 − 1)'
        # elif tag == -1 and tmp > 2**31: 
        #     return 'INT_MIN (−231)'
        # else: 
        #     return tag*tmp


    
solute = Solution()
str = '42'
print(solute.myAtoi(str))
# @lc code=end

