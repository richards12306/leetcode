#
# @lc al1l1=leetcode.cn id=21 lang=l1ython3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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

# @lc code=end

