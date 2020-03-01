# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# recursion
# Time: O(n), space: O(n) if counting stacks used for recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getLen(head):
            count = 0
            while head:
                count += 1
                head = head.next
            return count
        
        def add(l1, l2, offset):
            if not l1: return None
            if offset:
                node = ListNode(l1.val)
                nxt = add(l1.next, l2, offset - 1)
            else:
                node = ListNode(l1.val + l2.val)
                nxt = add(l1.next, l2.next, 0)
            if nxt and nxt.val > 9: # check nxt
                nxt.val %= 10
                node.val += 1
            node.next = nxt
            return node
            
        n1, n2 = getLen(l1), getLen(l2)
        head = ListNode(1)
        if n1 < n2: 
            l1, l2 = l2, l1
        head.next = add(l1, l2, abs(n1 - n2)) # abs
        if head.next.val > 9:
            head.next.val %= 10
            return head
        return head.next

# Using stacks
# Time: O(n), space: O(n)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getNums(head):
            s = []
            while head:
                s.append(head.val)
                head = head.next
            return s
        
        def addNumToList(num, nxt):
            carry = num // 10
            node = ListNode(num % 10)
            node.next = nxt
            return carry, node
        
        s1, s2 = getNums(l1), getNums(l2)
        carry = 0
        nxt = None
        while s1 and s2:
            num = s1.pop() + s2.pop() + carry
            carry, nxt = addNumToList(num, nxt)
        if s2: s1 = s2
        while s1:
            num = s1.pop() + carry
            carry, nxt = addNumToList(num, nxt)
        if carry:
            _, nxt = addNumToList(carry, nxt)
        return nxt
