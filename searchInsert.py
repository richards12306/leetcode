class Solution:
    def searchInsert(self, nums,target):
        for i in range(len(nums)):
            if target < nums[i]:
                return i
                break
            elif target == nums[i]:
                return i
                break

        return i+1
solute = Solution()
nums = [1,3,5,6]
target =  9
print(solute.searchInsert(nums,target))

