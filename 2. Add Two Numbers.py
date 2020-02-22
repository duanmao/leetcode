# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = l1, l2
        carry = 0
        head = node = ListNode(0)
        while n1 and n2:
            add = n1.val + n2.val + carry
            node.next = ListNode(add % 10)
            carry = int(add / 10)
            n1, n2, node = n1.next, n2.next, node.next
        n1 = n1 or n2
        while n1:
            add = n1.val + carry
            node.next = ListNode(add % 10)
            carry = int(add / 10)
            n1, node = n1.next, node.next
        if carry:
            node.next = ListNode(carry)
        return head.next
