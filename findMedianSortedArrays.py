class Solution:
    def findMedianSortedArrays(self, nums1,nums2):
        length_1, length_2 = len(nums1), len(nums2)
        length = length_2 + length_1
        frirst_index, second_index = 0, 0
        mid_number=[0,0]

        mid_index = (length + 1) // 2
        for i in range(mid_index+1):
            # if frirst_index < length_1 and second_index == length_2 or 
            if frirst_index == length_1 and second_index == length_2:
                return float(mid_number[0])
            if second_index < length_2:
                if frirst_index == length_1 or nums1[frirst_index] > nums2[second_index]:
                    mid_number=[nums2[second_index],mid_number[0]]
                    second_index += 1
                elif nums1[frirst_index] <= nums2[second_index]:
                    mid_number=[nums1[frirst_index],mid_number[0]]

                    frirst_index += 1
            elif second_index == length_2:
                mid_number=[nums1[frirst_index],mid_number[0]]
               
                frirst_index += 1



        







        #     if frirst_index < length_1 and second_index < length_2:
        #         if nums1[frirst_index] <= nums2[second_index]:


        #             mid_number[1] = mid_number[0]
        #             mid_number[0] = nums1[frirst_index]
        #             frirst_index += 1

        #         elif nums1[frirst_index] > nums2[second_index]:
        #             mid_number[1] = mid_number[0]
        #             mid_number[0] = nums2[second_index]
        #             second_index += 1
        #     elif frirst_index == length_1:
        #         mid_number[1] = mid_number[0]
        #         mid_number[0] = nums2[second_index]
        #         second_index += 1
        #     else:
        #         mid_number[1] = mid_number[0]
        #         mid_number[0] = nums1[frirst_index]
        #         frirst_index += 1



        # if length % 2 == 0:             #the length of two list is odd
        #     mid_number = (float(mid_number[0]) + float(mid_number[1]))/2
        # else:
        #     mid_number = float(mid_number[1])
        
        # return mid_number


nums1 = [3,4]
nums2 = [1,2]
solute=Solution()
print(solute.findMedianSortedArrays(nums1,nums2))



















