class Solution:
    def removeElement(self, nums,val):
        tag = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[tag] = nums[i]
                tag += 1
        nums = nums[:tag]
        print(nums)
        return tag

solute = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
print(solute.removeElement(nums,val))
