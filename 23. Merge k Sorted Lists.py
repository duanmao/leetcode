# Time: O(nklogk), space: O(k) where n is the average length of each list, k is the total number of lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import *
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        hp = [(head.val, head) for head in lists if head]
        heapify(hp)
        head = cur = ListNode(0)
        while (len(hp)):
            node = hp[0][1]
            if (node.next):
                heapreplace(hp, (node.next.val, node.next))
            else:
                heappop(hp)
            cur.next = node
            cur = cur.next
        return head.next

# Time: O(nk^2) where n is the average length of each list, k is the total number of lists
# n1 + n2
# n1 + n2 + n3
# n1 + n2 + n3 + n4
# ...
# n1 + n2 + n3 + ... + nk
# 
# sum = n1 * (k - 1) + n2 * (k - 1) + n3 * (k - 2) + ... nk * 1
# 	=> O(nk^2)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge(h1, h2):
            if (not h1 or not h2):
                return h1 or h2
            head = cur = None
            while (h1 and h2):
                if (h1.val < h2.val):
                    sml = h1
                    h1 = h1.next
                else:
                    sml = h2
                    h2 = h2.next
                if (not head):
                    head = sml
                else:
                    cur.next = sml
                cur = sml
            if (h1):
                cur.next = h1
            elif (h2):
                cur.next = h2
            return head
        
        if (not len(lists)):
            return None
        head = lists[0]
        for i in range(1, len(lists)):
            head = merge(head, lists[i])
        return head
