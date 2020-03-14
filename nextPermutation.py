#字典序 
class Solution:
    def nextPermutation(self, nums):
        length = len(nums)
        if length == 0:
            return [nums[1], nums[0]]
        a = -1
        for index in range(length-1,-1,-1):  
            if nums[index-1] < nums[index]:
                a = index - 1
                break
        if a == -1:
            nums.sort()
            return sort
        for index in range(length - 1, a, -1):
            if nums[index] > nums[a]:
                nums[index], nums[a] = nums[a], nums[index]
                nums_sort = nums[a+1:]
                nums_sort.sort()
                nums[a+1:] = nums_sort
                break

        return nums

solute=Solution()
nums = [1,2,3,4,6,5]
solute.nextPermutation(nums)
        

            