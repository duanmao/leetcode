# worst case O(n^2), average case O(n^1.5), hard for me to analysis though
# at first it seems O(n^3) to me.. but it's indeed empirically much faster
# though it depends on test cases as well
# the idea is to sort by column
# https://leetcode.com/problems/minimum-area-rectangle/solution/
# analysis in: https://leetcode.com/problems/minimum-area-rectangle/discuss/192021/Python-O(N1.5)-80ms
# leetcode.com/articles/minimum-area-rectangle/192096/Minimum-Area-Rectangle/310301
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        if nx == n or ny == n:
            return 0

        p = collections.defaultdict(list)
        # purely for time efficiency: the coming part is O(n*m^2), we want to minimize m
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)

        lastx = {}
        res = float('inf')
        for x in sorted(p):
            p[x].sort()
            for i in range(len(p[x])):
                for j in range(i):
                    y1, y2 = p[x][j], p[x][i]
                    if (y1, y2) in lastx:
                        res = min(res, (x - lastx[y1, y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return res if res < float('inf') else 0

# Time: O(n^2), space: O(n)
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        area = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if ((x1, y2) in seen and (x2, y1) in seen):
                    area = min(area, abs(x1 - x2) * abs(y1 - y2))
            seen.add((x1, y1))
        return area if area < float('inf') else 0

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points = set(map(tuple, points))
        area = float('inf')
        pointslist = list(points)
        for i, p1 in enumerate(pointslist):
            for j in range(i):
                x1, y1 = p1
                x2, y2 = p2 = pointslist[j]
                if (p1 == p2 or x1 == x2 or y1 == y2): continue
                if ((x1, y2) in points and (x2, y1) in points):
                    area = min(area, abs((x2 - x1) * (y2 - y1)))
        return area if area < float('inf') else 0
