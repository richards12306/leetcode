#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        res = []
        p = 0 # p, k, i, j
        while p < n - 3:  # 文中提到的条件1和条件2，可以直接跳过
            if nums[p] + 3 * nums[p + 1] > target: break  
            if nums[p] + 3 * nums[-1] < target:           
                while p < n - 4 and nums[p] == nums[p + 1]: p += 1
                p += 1
                continue
            k = p + 1
            while k < n - 2:   # k 和 p 的判断是一样的
                if nums[p] + nums[k] + 2 * nums[k + 1] > target: break
                if nums[p] + nums[k] + 2 * nums[-1] < target: 
                    while k < n - 3 and nums[k] == nums[k + 1]:
                        k += 1
                    k += 1
                    continue
                i = k + 1
                j = n - 1
                new_target = target - nums[p] - nums[k]
                while i < j:
                    if nums[i] + nums[j] > new_target: j -= 1
                    elif nums[i] + nums[j] < new_target: i += 1
                    else:
                        res.append([nums[p],nums[k],nums[i],nums[j]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i - 1]: i += 1 # 避免结果重复
                        while i < j and nums[j] == nums[j + 1]: j -= 1 # 避免结果重复
                while k < n - 3 and nums[k] == nums[k + 1]: k += 1
                k += 1
            while p < n - 4 and nums[p] == nums[p + 1]: p += 1
            p += 1
        return res


    #     nums.sort()
    #     result = []
    #     if len(nums)<4: 
    #         return []
    #     for index in range(0,len(nums)-3,1): 
    #         if index > 0  and nums[index] == nums[index-1]: 
    #             continue
    #         if nums[index] + 3*nums[index+1]>target:
    #             break
    #         threeLists = self.threeSum(nums[index+1:],target-nums[index])
    #         for threeList in threeLists: 
    #             threeList.append(nums[index])
    #             result.append(threeList)
    #     return result

    # def threeSum(self,nums,target): 
    #     result = []
    #     left,right = 0,len(nums)-1
    #     for index in range(0,len(nums)-2,1):
    #         if index > 0  and nums[index] == nums[index-1]: 
    #             continue
    #         if nums[index]+2*nums[index+1]>target: 
    #             break


    #         tempTarget = target - nums[index]
    #         left,right = index+1,len(nums)-1
    #         while left < right: 
    #             # while left+1<right and left>index+1 and nums[left] == nums[left-1]: 
    #             while left>index+1 and nums[left] == nums[left-1] and left < len(nums)-1:
    #                 left += 1
    #             # while right<len(nums)-2 and right-1>left and nums[right] == nums[right+1]: 
    #             while right<len(nums)-2 and nums[right] == nums[right+1] and right>index:
    #                 right -= 1
    #             if left >= right:
    #                 break


    #             if nums[left] + nums[right] == tempTarget: 
    #                 result.append([nums[index],nums[left],nums[right]])
    #                 left+=1
    #             elif nums[left] + nums[right] > tempTarget:
    #                 right-=1
    #             else: 
    #                 left+=1
    #     return result
nums = [-5,5,4,-3,0,0,4,-2]
target = 4
solute = Solution()
solute.fourSum(nums,target)            


    
# @lc code=end

