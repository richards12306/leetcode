#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start


class Solution:
    def countAndSay(self, n: int) -> str:
        first_str=''
        # count记录了连续相同的数
        count=1
        temp=''
        while(n>0):
            if first_str=='':
                first_str='1'
                n-=1
                continue
            if len(set(first_str))==1:
                first_str=str(len(first_str)*int(first_str[0]))+first_str[0]
                n-=1
                continue
            # 这样写循环虽然很反锁，但是思路还是挺清晰的
            for index in range(len(first_str)):
                # 如果两个相邻的数相等                 
                if first_str[index+1]==first_str[index]:
                    # 如果为最后两个数，例如 1,1
                    if (index+1)==len(first_str)-1:
                        count+=1
                        temp+=str(count)+first_str[index]
                        first_str=temp
                        n-=1
                        temp=''
                        count=1
                        break
                    # 不为最后两个数
                    else:
                        count+=1
                 # 如果两个相邻的数不相等
                else:
                    # 如果最后两个数不相等，例如 2,1
                    if(index+1)==len(first_str)-1:
                        temp+=str(count)+first_str[index]
                        # 因为最后一个字符肯定为 1
                        first_str=temp+'11'
                        n-=1
                        temp=''
                        count=1
                        break
                    # 不是最后两个数，且相邻两个数不等，重新计数
                    else:
                        temp+=str(count)+first_str[index]
                        count=1
        return first_str



# @lc code=end

        tag = 1
        result = "11"
        currentResult = ""
        for j in range(n - 1):
            i = 1
            while i < len(result):

                if result[i] == result[i - 1]:
                    tag += 1
                    if i == len(result) - 1:
                        currentResult = currentResult.join(
                            str(tag) + str(result[i - 1]))
                    print(currentResult)

                elif i == 1:
                    currentResult = result[0]
                else:
                    currentResult = currentResult.join(
                        str(tag) + str(result[i - 1]))
                    print(currentResult)
                i += 1
            result = currentResult
        return result
