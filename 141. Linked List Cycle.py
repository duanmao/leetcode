# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        n1, n2 = head, head.next
        while n1 and n2:
            if n1 == n2: return True
            n1, n2 = n1.next, n2.next
            if n2: n2 = n2.next
        return False
