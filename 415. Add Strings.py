class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l = max(len(num1), len(num2))
        num1, num2 = num1.zfill(l), num2.zfill(l)
        res = ""
        carry = 0
        for i in reversed(range(l)):
            add = int(num1[i]) + int(num2[i]) + carry
            carry = int(add / 10)
            res = str(add % 10) + res
        if carry: res = str(carry) + res
        return res
