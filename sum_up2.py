#!/usr/bin/python3
# -*- coding: UTF-8 -*-
class Solution:
    # def twoSum(self,order_list,target):#hash 数组法

    #     hash_list = {}
    #     for index, value in enumerate(order_list):
    #         if hash_list.get(target-value) != None:
    #             return[hash_list[target-value], index]
    #         hash_list[value]=index
    def twoSum(self,order_list,target):
        i=0
        j=len(order_list)-1
        while i != j:
            sum=order_list[i]+order_list[j]
            if sum == target:
                return [i,j]
            if sum < target:
                i+=1
            else:
                j-=1


order_list = [2, 7, 11, 15]
target = 9
solute = Solution()
print(solute.twoSum(order_list,target))
