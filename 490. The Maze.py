# BFS
# Time and space O(mn)
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if (not maze): return False
        m, n = len(maze), len(maze[0])

        def wall(r, c):
            if (r < 0 or c < 0 or r >= m or c >= n): return True
            else: return maze[r][c]

        direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = collections.deque()
        queue.append(start)
        added = {(start[0], start[1])}
        while (queue):
            r, c = queue.popleft()
            for dx, dy in direc:
                x, y = r, c
                while (not wall(x + dx, y + dy)):
                    x += dx
                    y += dy
                if ([x, y] == destination): return True
                if ((x, y) not in added):
                    added.add((x, y))
                    queue.append((x, y))
        return False

# DFS with memo, slightly slower than the previous one
# cleaner: https://leetcode.com/problems/the-maze/discuss/150523/Python-elegant-DFS-solution
# Time and space O(mn)
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if (not maze): return False
        m, n = len(maze), len(maze[0])
        
        def wall(r, c):
            if (r < 0 or c < 0 or r >= m or c >= n): return True
            else: return maze[r][c]
            
        direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # please remember to record visited nodes, PLEASE!!! otherwise it'll loop FOREVER!!!
        # You're making the same mistake every time!!!!! every time you do DFS!!! Unacceptable!!!
        starts = {} # store checked starting points and their results
        def canReach(frm):
            sr, sc = frm
            if (frm == destination): starts[(sr, sc)] = True
            if ((sr, sc) in starts): return starts[(sr, sc)]
            starts[(sr, sc)] = False
            for k in range(4):
                r, c = frm
                while (not wall(r + direc[k][0], c + direc[k][1])):
                    r += direc[k][0]
                    c += direc[k][1]
                if ([r, c] != frm and canReach([r, c])):
                    starts[(sr, sc)] = True
                    break
            return starts[(sr, sc)]
        
        return canReach(start)

# same BFS, but much slower than the previous one lol, put it here cause it's worth comparison
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if (not maze): return False
        m, n = len(maze), len(maze[0])
        
        def wall(r, c):
            if (r < 0 or c < 0 or r >= m or c >= n): return True
            else: return maze[r][c]
            
        direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        queue = collections.deque()
        queue.append(start)
        visited = set()
        while (queue):
            r, c = queue.popleft()
            visited.add((r, c))
            if ([r, c] == destination): return True
            for dx, dy in direc:
                x, y = r, c
                while (not wall(x + dx, y + dy)):
                    x += dx
                    y += dy
                if ((x, y) not in visited):
                    queue.append((x, y))
        return False
