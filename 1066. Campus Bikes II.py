# Heap
# 什么奇技淫巧...
# Time: not sure but.. for the heap worst case should contain exponential states, so it's
# exponential I guess?
# Just in case: https://leetcode.com/problems/campus-bikes-ii/discuss/303422/Python-Priority-Queue
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def distance(w, b):
            return abs(b[0] - w[0]) + abs(b[1] - w[1])

        heap = [(0, 0, 0)] # accumulated distance, worker to assign, bikes assignment states
        visited = set()
        while (True):
            dis, wi, states = heapq.heappop(heap)
            if (wi == len(workers)): return dis
            if (states in visited): continue
            visited.add(states)
            for j, b in enumerate(bikes):
                # we use the j-th bit in states to denote whether bikes[j] has been assigned
                # 1 means it's already assigned before, 0 means it's still available
                # if it's not assigned, we assign it to the current worker wi
                # record the total distance in heap, and move onto the next worker wi + 1
                if (not states & (1 << j)): # if this bike has not been assigned
                    heapq.heappush(heap, (dis + distance(workers[wi], b), wi + 1, states | (1 << j)))
        return 0

# DP
# the states marking is the same as the above one: using bits as the indicator of assignment
# this kind of bit masking and states recording techniques is insane...!!!
# f[i][s] = the min distance for first i workers to build the state s
# f[i][s] = min(f[i][s], f[i - 1][prev] + dis(w[i-1], bike[j)) for 0 <= j < n, prev = s ^ (1 << j)
# Time: exponential, O(2^n) where n is the # of bikes
# https://leetcode.com/problems/campus-bikes-ii/discuss/305218/DFS-%2B-Pruning-And-DP-Solution
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def distance(w, b):
            return abs(b[0] - w[0]) + abs(b[1] - w[1])

        m, n = len(workers), len(bikes)
        # f[i][s] = the min distance for first i workers to build the state s
        f = [[float('inf')] * (1 << n) for i in range(m + 1)]
        f[0][0] = 0 # initialization
        for i in range(1, m + 1):
            for s in range(1 << n):
                if f[i - 1][s] == float('inf'): continue # invalid state
                for j, b in enumerate(bikes):
                    if (s & (1 << j)): continue # bike is already assigned
                    sn = s | (1 << j)
                    f[i][sn] = min(f[i][sn], f[i - 1][s] + distance(workers[i - 1], b))
        return min(f[m])

# TLE - Brute force DFS
# Time: O(m * n!), m is number of workers, n is number of bikes
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        self.mindis = float('inf')

        def distance(w, b):
            return abs(b[0] - w[0]) + abs(b[1] - w[1])

        def dfs(wi, assigned, curdis):
            if (wi == len(workers)):
                self.mindis = min(self.mindis, curdis)
                return
            if (curdis > self.mindis): return
            for j, b in enumerate(bikes):
                if (not assigned[j]):
                    assigned[j] = True
                    dfs(wi + 1, assigned, curdis + distance(workers[wi], b))
                    assigned[j] = False

        assigned = [False] * len(bikes)
        dfs(0, assigned, 0)
        return self.mindis

# BTW here's a INCREDIBLY fast solution, fast like CRAZY!!! but too long to understand right now
# let's leave it as TODO (which very likely also means never do...)
# https://leetcode.com/problems/campus-bikes-ii/discuss/305160/Python-Minimum-cost-flow-beat-97
