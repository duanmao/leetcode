# one pass. Time: O(n), space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        for i in range(n):
            fast = fast.next
        pre = None
        cur = head
        while (fast):
            pre = cur
            cur = cur.next
            fast = fast.next
        if (pre):
            pre.next = cur.next
        else:
            head = cur.next
        return head

# 2 passes. Time: O(n), space: O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        total = 0
        cur = head
        while (cur):
            total += 1
            cur = cur.next
        cur = head
        pre = None
        for i in range(total - n):
            pre = cur
            cur = cur.next
        if (pre):
            pre.next = cur.next
        else:
            head = cur.next
        return head
