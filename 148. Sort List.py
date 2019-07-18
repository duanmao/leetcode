# Time: O(nlogn), space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(h1, h2):
            if (not h1 or not h2):
                return h1 or h2
            head = node = None
            while (h1 and h2):
                if (h1.val < h2.val):
                    cur = h1
                    h1 = h1.next
                else:
                    cur = h2
                    h2 = h2.next
                if (not head):
                    head = cur
                else:
                    node.next = cur
                node = cur
            node.next = h1 or h2
            return head
            
        if (not head or not head.next): # must check head.next
            return head
        slow = fast = head
        pre = None
        while (fast and fast.next):
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if (pre): # remember check pre
            pre.next = None # the most brilliant step (stolen from others) IMO
        left = self.sortList(head)
        right = self.sortList(slow)
        return merge(left, right)
