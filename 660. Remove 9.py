# Time: O(log(9)n), space: O(1)
class Solution:
    def newInteger(self, n: int) -> int:
        # all the valid numbers are base-9 numbers, and every base-9 number is a legal number here
        # thus this question, equivalently, is asking for the nth number in the base-9 sequence
        # so we just follow the process of converting a decimal number to a base-k number
        res = ""
        while (n):
            res = str(n % 9) + res
            n //= 9
        return res
