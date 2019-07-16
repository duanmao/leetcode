# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time: O(n), space: O(1)
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while (fast):
            if (slow):
                slow = slow.next
            if (fast):
                fast = fast.next
                if (fast):
                    fast = fast.next
                    if (slow == fast):
                        return True
        return False

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (not head):
            return False
        slow = head
        fast = head.next
        while (fast):
            if (slow == fast):
                return True
            if (slow):
                slow = slow.next
            if (fast):
                fast = fast.next
                if (fast):
                    fast = fast.next
        return False
