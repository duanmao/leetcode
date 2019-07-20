# Time: O(nlogn), space: O(n)
# detailed explanation: https://leetcode.com/problems/the-skyline-problem/discuss/61197/(Guaranteed)-Really-Detailed-and-Good-(Perfect)-Explanation-of-The-Skyline-Problem
from heapq import *
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = [] # [(x, y, x' which is the other edge of this building)]
        for bld in buildings:
            # the most genius idea to use -bld[2] and it's a must-have!
            # the reason is to break tie when the first numbers are equal
            # i.e. two left points have the same x coordinates
            # in this case, the higher one should be considered first
            # so that the lower one will be skipped as a legitmate skyline key point
            points.append((bld[0], -bld[2], bld[1])) 
            # but for right points, the tie breaker is exactly opposite
            # when two right points have the same x coordinates
            # still it's the lower one that should be excluded from key points
            # but this time it must come first in order to be skipped
            # this two tie breakers are too critical to be overemphasized!!
            points.append((bld[1], bld[2], bld[0]))
        points.sort()
        hp = [] # a max heap to keep the heights
        skyline = []
        prevh = 0
        for x, y, xo in points:
            if (y < 0): # a left point
                heappush(hp, (y, x, xo))
            else: # a right point
                while (len(hp) and hp[0][2] <= x):
                # pop out all larger heights as long as it belong to buildings 
                # that have already been passed
                # i.e. the right edge of the building is lte (<=) the current x
                    heappop(hp)
            curh = -hp[0][0] if len(hp) else 0 # current max height
            if (not curh == prevh):
            # if the max height has changed, a key point is found
                skyline.append([x, curh])
            prevh = curh
        return skyline

# A much shorter/concise version
from heapq import *
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = sorted([(L, -H, R) for L, R, H in buildings] + [(R, 0, None) for _, R, _ in buildings])
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in points:
            while x >= hp[0][1]: 
                heappop(hp)
            if negH: 
                heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]: 
                res.append([x, -hp[0][0]])
        return res[1:]
