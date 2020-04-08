# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next: # need to stop when fast.next == None
            fast = fast.next.next if fast.next else fast.next
            slow = slow.next
        return slow
