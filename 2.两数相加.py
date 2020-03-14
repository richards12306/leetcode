#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a,b = 0,0
        tag = 0

        
        while l1:

            a = a+l1.val * 10**tag
            l1 = l1.next
            tag +=1
        tag = 0

        while l2:
            b = b+l2.val * 10**tag
            l2 = l2.next
            tag +=1
        r = a + b
        re = ListNode(r - r//10*10)
        result = re
        r=r//10
        
        while r!=0:
            re.next = ListNode(r - r//10*10)
            r = r//10
            re = re.next
        return result      
# @lc code=end

a=ListNode(0)

b=ListNode(1)

solute = Solution()
print(solute.addTwoNumbers(a,b))