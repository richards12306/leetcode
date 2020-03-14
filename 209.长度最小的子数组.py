#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s, nums):
        #依旧是分治法，一个字符串从中间分开，满足情况的字符串： 左边，右边，包含中间元素。【事实上这个方法写的我很不开心
        #决定搞完这个用暴力试一试
        if len(nums) == 0:
            return 0
        result = [0]
        sumup = 0
        for index in nums:
            sumup = sumup + index
            result.append(sumup)

        r,l = 0,0
        length =len(result)
        minlength = len(result)
        while True:
            if r<length and l<=r :
                if result[r]-result[l]>=s:
                    minlength = min([minlength,r-l])
                    l+=1
                else:
                    r+=1
            
            else:
                if minlength == len(result):
                    return 0
                else:
                    return minlength

solute =Solution()
nums = [2,3,1,2,4,3]
s=7
solute.minSubArrayLen(s,nums)

    

# @lc code=end

# if len(nums)==0:
#             return 0
#         if len(nums) ==1:
#             if nums[0] > s:
#                 return 1
#             else:
#                 return 0
#         minLeft = self.minSubArrayLen(s,nums[:len(nums)//2])
#         minRight = self.minSubArrayLen(s,nums[len(nums)//2:])
#         minMiddle = 0
#         sumup = 0
#         lindex, rindex = len(nums)//2-1,len(nums)//2


#         while lindex>-1 or rindex<=len(nums):
#             if lindex <0 and rindex >=len(nums):
#                 minMiddle = 0
#                 break
#             elif lindex<0 or nums[lindex] <nums[rindex]:
#                 sumup = sumup + nums[rindex]
#                 rindex += 1
#             elif rindex==len(nums) or nums[lindex] >= nums[rindex]:
#                 sumup = sumup + nums[lindex]
#                 lindex -= 1
            
#             minMiddle += 1
#             if sumup >= s:
#                 break

#         result = [minLeft,minRight,minMiddle]
#         result = list(filter(lambda number : number > 0,result))
#         if len(result)>0:
#             return min(result)
#         else:
#             return 0