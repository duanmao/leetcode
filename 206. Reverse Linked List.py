# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        node = head.next
        while node:
            head.next = node.next
            node.next = dummy.next
            dummy.next = node
            node = head.next
        return dummy.next
