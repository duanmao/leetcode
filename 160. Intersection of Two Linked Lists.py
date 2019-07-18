# Time: O(n), space: O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        node1 = headA
        node2 = headB
        while (node1 and node2):
            node1 = node1.next
            node2 = node2.next
        if (not node1):
            longer = headB
            shorter = headA
            contin = node2
        else:
            longer = headA
            shorter = headB
            contin = node1
        while (contin):
            longer = longer.next
            contin = contin.next
        while (not shorter == longer):
            shorter = shorter.next
            longer = longer.next
        return longer
