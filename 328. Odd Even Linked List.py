# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next: return head
        odd, even, cur = head, head.next, head.next.next
        while even and cur:
            even.next = cur.next
            cur.next = odd.next
            odd.next = cur
            odd = cur
            even = even.next
            if even: cur = even.next
        return head
