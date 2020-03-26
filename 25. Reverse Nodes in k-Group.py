# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverseK(start, k):
            node = start
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            if count < k: return start, None
            tail = start
            node = start.next
            while k > 1:
                tail.next = node.next
                node.next = start
                start = node
                node = tail.next
                k -= 1
            return start, tail
            
        dummy = node = ListNode(0)
        dummy.next = head
        while node:
            node.next, node = reverseK(node.next, k)
        return dummy.next
