class Solution:
    def searchRange(self, nums,target):
        begin, end = 0, len(nums)-1
        while begin <= end:
            index = (begin + end + 1) // 2
            if target < nums[index]:
                end = index - 1
                
            elif target > nums[index]:
                begin = index + 1
            elif target == nums[index]:
                print(index)
                begin, end = index ,index

                
                while begin >= 0 and nums[begin] == target:
                    begin -= 1
                while end < len(nums) and nums[end] == target:
                    end +=1
                return [begin+1, end-1]

        return [-1,-1]
                    
nums = [1,3]
target = 1
solute = Solution()
print(solute.searchRange(nums,target))

