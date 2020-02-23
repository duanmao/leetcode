# two pointers
# Time: O(n), space: O(1)
# https://leetcode.com/problems/trapping-rain-water/discuss/17357/Sharing-my-simple-c%2B%2B-code%3A-O(n)-time-O(1)-space
# https://leetcode.com/problems/trapping-rain-water/solution/ Approach 4
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        lmax = rmax = 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                lmax = max(lmax, height[left])
                water += lmax - height[left]
                left += 1
            else:
                rmax = max(rmax, height[right])
                water += rmax - height[right]
                right -= 1
        return water

# DP
# Time: O(n), space: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        left, right = [height[0]] + [0] * (n - 1), [0] * (n - 1) + [height[n - 1]]
        water = 0
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
            water += min(left[i], right[i]) - height[i]
        return water

# mono stack
# Time: O(n), space: O(n)
# https://leetcode.com/problems/trapping-rain-water/discuss/17414/A-stack-based-solution-for-reference-inspired-by-Histogram
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        s = []
        water = 0
        for i, h in enumerate(height):
            while s and height[s[-1]] <= h:
                curidx = s.pop()
                if s:
                    lidx = s[-1]
                    water += (i - lidx - 1) * (min(height[lidx], height[i]) - height[curidx])
            s.append(i)
        
        return water
