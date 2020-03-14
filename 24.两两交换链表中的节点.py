#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: 
            return head
        preNode = ListNode(-1)
        preNode.next = head
        current = preNode
        # print(current.val,current.next)
        middleNode = head 
        nextNode = head.next

        while nextNode: 
            preNode.next = middleNode.next
            middleNode.next = nextNode.next
            nextNode.next = middleNode
            # print(preNode.val,middleNode.val,nextNode.val)
            preNode = middleNode
            middleNode = preNode.next
            if not middleNode: 
                return current.next
            nextNode = middleNode.next

        return current.next
# @lc code=end

