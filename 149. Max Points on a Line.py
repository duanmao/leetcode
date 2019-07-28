# Time: O(n^2), space: O(n^2)
import math
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if (len(points) == 1): # special handle for single point
            return 1
        slopes = {}
        maxcount = 0
        for i, (x1, y1) in enumerate(points):
            overlap = 0
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                ydiff, xdiff = y2 - y1, x2 - x1
                key = None
                if (xdiff == 0 and not ydiff == 0):
                    key = (0, 0)
                else:
                    if (ydiff == 0 and xdiff == 0): # mind overlapping points
                        overlap += 1
                    else:
                        dvs = math.gcd(ydiff, xdiff)
                        neg = (ydiff < 0) ^ (xdiff < 0)
                        ydiff = abs(ydiff) if not neg else -abs(ydiff)
                        key = (ydiff // dvs, abs(xdiff) // dvs)
                if (key):
                    if (key not in slopes):
                        slopes[key] = 2
                    else:
                        slopes[key] += 1
            if (slopes):
                maxcount = max(maxcount, max(slopes.values()) + overlap)
                slopes.clear()
            else:
                maxcount = max(maxcount, overlap + 1)
        return maxcount
