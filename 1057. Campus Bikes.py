# Time: O(mn), space: O(mn)
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        bucket = [[] for i in range(2001)] # max distance 2000
        for i, [wx, wy] in enumerate(workers):
            for j, [bx, by] in enumerate(bikes):
                dis = abs(wx - bx) + abs(wy - by)
                bucket[dis].append((i, j))
        n = len(workers)
        assign = [-1] * n
        assigned = set()
        for dis in bucket:
            for w, b in dis:
                if (assign[w] == -1 and b not in assigned):
                    assign[w] = b
                    assigned.add(b)
                if (len(assigned) == n):
                    return assign
        return assign

# If the distance range cannot be determined:
# https://leetcode.com/problems/campus-bikes/discuss/303906/Python-heap-of-closest-bike-to-each-worker
from heapq import *
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        dist_wbpairs = collections.defaultdict(list)
        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                dist = abs(wx - bx) + abs(wy - by)
                dist_wbpairs[dist].append((i, j))

        dists = list(dist_wbpairs.keys())
        heapify(dists)
        ans = [-1] * len(workers)
        paired = 0
        assigned = [False] * len(bikes)
        while (dists):
            dist = heappop(dists)
            wbpairs = dist_wbpairs[dist]
            for w, b in wbpairs:
                if (ans[w] == -1 and not assigned[b]):
                    ans[w] = b
                    assigned[b] = True
                    paired += 1
                if (paired == len(workers)): return ans
        return ans
