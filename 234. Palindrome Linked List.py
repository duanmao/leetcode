# Time: O(n), space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        revHead = None
        while (fast and fast.next):
            fast = fast.next.next
            nxt = slow.next
            slow.next = revHead
            revHead = slow
            slow = nxt
        if (fast): # odd number of nodes
            slow = slow.next
        while (slow):
            if (not slow.val == revHead.val):
                return False
            slow = slow.next
            revHead = revHead.next
        return True
