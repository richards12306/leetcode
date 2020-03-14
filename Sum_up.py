#!/usr/bin/python3
# -*- coding: UTF-8 -*-
class Solution:
    def twoSum(self,nums,target):
        hashmap={}
        
        for index, number in enumerate(nums):
            if hashmap.get(target-number) != None:
                return[hashmap[target-number],index]
            hashmap[number] = index


solute=Solution()
nums=[3,3]
target=6

print(solute.twoSum(nums,target))






