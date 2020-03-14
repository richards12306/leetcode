#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head: 
            return head
        # preNode = ListNode(-1)
        # preNode.next = head
        kList = []
        node = head
        reverseNode=ListNode(-1)
        current = reverseNode
        # reverseNode = reverseNode.next
        while True: 
            firstnode = node
            kList=[]
            for i in range(k):
                if node: 
                    kList.append(node)
                    node = node.next
                else: 
                    reverseNode.next = firstnode
                    return current.next
            # print(kList)
            for i in range(len(kList)-1,-1,-1): 
                # print(kList[i].val)
                reverseNode.next = kList[i]
                reverseNode = reverseNode.next
            
        return current
# @lc code=end

