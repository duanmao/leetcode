class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        mul5 = 5
        while (mul5 <= n):
            count += math.floor(n / mul5)
            mul5 *= 5
        return count

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while (n / 5):
            count += math.floor(n / 5)
            n /= 5
        return count
