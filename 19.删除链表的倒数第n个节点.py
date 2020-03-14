#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #双指针，后一个比前一个晚 n+1 位
        #好吧，这个看上去应该用的少，但是其实一点也不少，我枯了，可能数据量不够大把
        preNode = nextNode = head
        for i in range(n): 
            nextNode = nextNode.next
            if nextNode == None: 
                return preNode.next
        
        while(nextNode.next): 
            nextNode = nextNode.next
            preNode = preNode.next
    
        preNode.next = preNode.next.next
        return head








        
# @lc code=end

#使用了一个列表保存所有链表的位置，但是这样占据空间太大了
        # nodeList = []
        # count = 0
        # while head: 
        #     nodeList.append(head)
        #     count+=1
        #     head = head.next
        # #removeNode = nodeList[len(nodeList)-n]
        # if n == len(nodeList): 
        #     if len(nodeList) == 1: 
        #         return None
        #     else: 
        #         return nodeList[1]
        # else: 
        #     nodeList[len(nodeList)-n-1].next = nodeList[len(nodeList)-n].next
        #     return nodeList[0]