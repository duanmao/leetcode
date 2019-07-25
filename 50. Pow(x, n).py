# Time: O(logn)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def mypow(x, n):
            if (n == 0):
                return 1
            elif (n == 1):
                return x
            half = self.myPow(x, n // 2)
            return half * half * (x if n % 2 else 1)
        return mypow(x, n) if n >= 0 else 1 / mypow(x, -n)
