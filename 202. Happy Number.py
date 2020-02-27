# Time: O(logn)
# as finding the next value for a given number has a cost of O(logn)
# because we are processing each digit in the number, and the number of digits is given by logn
# and the total number of possible numbers we would encounter is either a constant or bounded by
# logn as well. detailed analysis:
# https://leetcode.com/problems/happy-number/solution/
# space: O(1)
class Solution:
    def isHappy(self, n: int) -> bool:
        def digitsSquaresSum(n):
            ssum = 0
            while n:
                ssum += (n % 10) ** 2
                n = int(n / 10)
            return ssum
        
        slow, fast = n, digitsSquaresSum(n)
        while slow != fast and fast != 1:
            slow = digitsSquaresSum(slow)
            fast = digitsSquaresSum(digitsSquaresSum(fast))
        return fast == 1
