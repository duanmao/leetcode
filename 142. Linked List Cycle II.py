# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time: O(n), space: O(1)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next: return None
        l1, l2 = head.next, head.next.next
        while l1 and l2:
            if l1 == l2: break
            l1 = l1.next
            l2 = l2.next.next if l2.next else l2.next
        if not l2: return None
        l2 = head
        while l1 != l2:
            l1 = l1.next
            l2 = l2.next
        return l2
