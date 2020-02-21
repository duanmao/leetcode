


# DP
# Time: O(n), space: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        left, right = [height[0]] + [0] * (n - 1), [0] * (n - 1) + [height[n - 1]]
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        water = 0
        for i in range(n):
            water += min(left[i], right[i]) - height[i]
        return water
