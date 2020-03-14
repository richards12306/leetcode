class Solution:
    def search(self, nums, target):
        begin, end = 0, len(nums)-1
        if end == -1:
            return -1
        if nums == nums[0]:
            return 0

        while begin <= end:
            index = (begin + end + 1) // 2
            if target == nums[index]:
                return index
            elif target > nums[index]:
                if nums[index] > nums[0]:
                    begin = index + 1
                elif target < nums[0]:
                    begin = index + 1
                else:
                    end = index - 1


            elif target < nums[index]:
                if nums[index] <= nums[0]:
                    end = index - 1

                elif target < nums[0]:
                    begin = index + 1
                    
                elif target > nums[0]:
                    end = index -1




        return -1





nums = [1,3]
target = 1
solute = Solution()
print(solute.search(nums,target))
        



                
                    
                    

            