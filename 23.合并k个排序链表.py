#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        if len(lists)==0: 
            return None
        def mergeTwoLists(l1,l2): 
            current = ListNode(-1)
            mainNode = current
            while l1 and l2: 
                if l1.val <= l2.val: 
                    mainNode.next = l1
                    l1 = l1.next

                else:
                    mainNode.next = l2
                    l2 = l2.next

                mainNode = mainNode.next
            mainNode.next = l1 if l1 is not None else l2
            return current.next
            
        while len(lists)>1: 
            current = []
            for i in range(len(lists)//2): 
                current.append(mergeTwoLists(lists[i*2],lists[i*2+1]))
            if len(lists)%2 != 0: 
                current.append(lists[-1])
            lists = current
            print(lists)

        return lists[0]

            
# @lc code=end

   