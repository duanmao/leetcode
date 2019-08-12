# O(nlogn)
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/solution/
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if (not points): return 0
        points = sorted(points, key = lambda p: p[1])
        arrows = 1
        cur_end = points[0][1]
        for s, e in points:
            if (s > cur_end):
                arrows += 1
                cur_end = e
        return arrows
