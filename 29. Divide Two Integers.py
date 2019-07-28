# Time: O((logn)^2), space: O(1)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = False
        if ((dividend < 0) ^ (divisor < 0)):
            # print(dividend, divisor, "neg")
            neg = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while (dividend >= divisor):
            i = 1
            while (divisor * i <= dividend):
                i <<= 1
            i >>= 1
            res += i
            dividend -= divisor * i
            # print(res, dividend)
        res = res if not neg else -res
        # stupid stuff just to pass the OJ
        # res = res if res <= 2147483647 else 2147483647
        # res = res if res >= -2147483648 else -2147483648
        return res
