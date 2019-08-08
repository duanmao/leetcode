# Time: O(logn), space: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while (low <= high):
            mid = (low + high) // 2
            if (mid ** 2 <= x < (mid + 1) ** 2):
                return mid
            elif (mid ** 2 < x):
                low = mid + 1
            else:
                high = mid - 1
        return high
