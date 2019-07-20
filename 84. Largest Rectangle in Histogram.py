# Time: O(n), space: O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        maxArea = 0
        for i, h in enumerate(heights):
            leftx = i
            while (len(s) and s[-1][1] >= h):
                leftx, lefth = s.pop()
                maxArea = max(maxArea, (i - leftx) * lefth)
            s.append((leftx, h))
        right = len(heights)
        while (len(s)):
            leftx, lefth = s.pop()
            maxArea = max(maxArea, (right - leftx) * lefth)
        return maxArea
