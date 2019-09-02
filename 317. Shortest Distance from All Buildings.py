# https://leetcode.com/problems/shortest-distance-from-all-buildings/discuss/76891/Java-solution-with-explanation-and-time-complexity-analysis
# BFS with pruning
# Time: O(m^2*n^2), space: O(mn)
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if (not grid): return 0
        direcs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        m, n = len(grid), len(grid[0])
        distance = [[0] * n for i in range(m)]
        reach = [[0] * n for i in range(m)]
        
        def getDistance(si, sj, bdcount):
            added = [[False] * n for i in range(m)]
            queue = collections.deque([(si, sj, 0)])
            while (queue):
                curi, curj, curdis = queue.popleft()
                for mi, mj in direcs:
                    i, j = curi + mi, curj + mj
                    if (0 <= i < m and 0 <= j < n and
                        grid[i][j] == 0 and not added[i][j] and reach[i][j] == bdcount):
                        distance[i][j] += curdis + 1
                        reach[i][j] += 1
                        queue.append((i, j, curdis + 1))
                        added[i][j] = True
                        
        buildings = 0
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 1): # a building
                    getDistance(i, j, buildings)
                    buildings += 1
                    
        mindis = float('inf')
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 0 and reach[i][j] == buildings):
                    mindis = min(mindis, distance[i][j])
        return mindis if mindis < float('inf') else -1
