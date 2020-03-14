class Solution:
    def removeDuplicates(self, nums):
        tag=0
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                tag += 1
                nums[tag] = nums[i]
        
        nums = nums[:tag+1]
        print(nums)
        return tag + 1
                

solute = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]

print(solute.removeDuplicates(nums))

            
            