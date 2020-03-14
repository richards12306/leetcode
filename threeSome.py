class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    # def threeSum(self, nums):
    #     result=[]
    #     for first in range(len(nums)):
    #         for second in range(1,len(nums) - first - 1) :
    #             second = first + second
    #             for third in range(1,len(nums) - first - second -1 ):
    #                 third = second + third
    #                 if nums[third] + nums[first] + nums[second] == 0:
    #                     result.append([nums[first],nums[second],nums[third]])
    #     return result


    # def threeSum(self, nums):
    #     result_list=[]
    #     nums.sort()
    #     hash_map={}
    #     for i in range(len(nums)):
    #         begin, end = i+1, len(nums)-1
    #         while begin < end:
    #             result = nums[i] + nums[begin] + nums[end]
    #             if result == 0 :
    #                 k=[nums[begin] , nums[i] , nums[end]]
    #                 k.sort()
    #                 result_list.append(k)
    #                 break

    #             elif result < 0:
    #                 begin +=1
    #             elif result > 0:
    #                 end -=1

    #     return result_list

    def threeSum(self, nums):
        nums.sort()
        res =[]
        lennums= len(nums)
 
        for i in range(lennums):
            left =i+1
            right =lennums-1
            
            if i>0 and nums[i-1]==nums[i]:
                continue
            
            while left<right:
                sumthree = nums[i]+nums[left]+nums[right]
                if sumthree==0:
                    res_col = [nums[i],nums[left],nums[right]]
                    res.append(res_col)
                    left+=1
                    right-=1
                    
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                    while nums[right]==nums[right+1] and left<right:
                        right-=1
                              
                if sumthree<0:
                    left+=1
                if sumthree>0:
                    right-=1
        return res
    




solute=Solution()
nums=[-2,-2,0,0,1,1,1]
print(solute.threeSum(nums))

