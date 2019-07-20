# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1 or not l2):
            return l1 or l2
        ans = cur = ListNode(0)
        carry = 0
        while (l1 and l2):
            s = l1.val + l2.val + carry
            carry = int(s / 10)
            cur.next = ListNode(s % 10)
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        l = l1 or l2
        while (l):
            s = l.val + carry
            carry = int(s / 10)
            cur.next = ListNode(s % 10)
            l = l.next
            cur = cur.next
        if (carry):
            cur.next = ListNode(carry)
        return ans.next
