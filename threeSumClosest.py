class Solution:
    def threeSumClosest(self, nums,target):
        min_list = []
        nums.sort()
        min_distance = abs(nums[0] + nums[1] + nums[2] - target)
        min_sum_up = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-1):
            begin, end = i+1, len(nums)-1
            while begin < end:
                sum_up = nums[begin] + nums[i] + nums[end]
                distance = sum_up - target
                abs_distance = abs(distance)
                if abs_distance == 0 :
                    min_sum_up = sum_up
                    return min_sum_up
                elif abs_distance < min_distance:
                    min_distance = abs_distance
                    min_sum_up = sum_up


                if distance < 0 :
                    begin += 1 
                elif distance > 0 :
                    end -= 1

        return min_sum_up
solute = Solution()
nums = [1,1,1,0]
target = -100
print(solute.threeSumClosest(nums,target))
                

        
    