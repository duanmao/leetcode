# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def swap(pre, n1, n2):
            pre.next = n2
            n1.next = n2.next
            n2.next = n1
            return n1
            
        if not head: return head
        n1, n2 = head, head.next
        pre = ListNode(0)
        pre.next = head
        head = pre
        while n1 and n2:
            pre = swap(pre, n1, n2)
            n1 = pre.next
            if n1: n2 = n1.next
        return head.next
