#Solution:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry, res_head = 0, ListNode(0)
        res_it = res_head
        while l1 or l2 or carry > 0:
            x, y = l1.val if l1 else 0, l2.val if l2 else 0
            r = x + y + carry
            if r >= 10: r, carry = r - 10, 1
            else: carry = 0
            res_it.next = ListNode(r)
            res_it = res_it.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return res_head.next
