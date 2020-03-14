#!/usr/bin/python3
# -*- coding: UTF-8 -*-
class Solution:
    def maxArea(self, height: list[int]) -> int:
        begin = 0
        end = len(height)-1
        MaxArea = 0

        while begin != end :
            Area = min([height[begin],height[end]]) * (end - begin)
            MaxArea = max([Area,MaxArea])

        return MaxArea

height=[1,8,6,2,5,4,8,3,7]
solute=Solution()
print(solute.maxArea(height))