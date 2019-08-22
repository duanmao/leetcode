class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if (not stones): return True
        steps = {} # the legit steps we can jump on each stone
        for stone in stones: steps[stone] = set()
        steps[stones[0]].add(1)
        for on in stones:
            for step in steps[on]:
                jumpto = on + step
                if (jumpto == stones[-1]): return True
                if (jumpto in steps):
                    for k in range(-1, 2):
                        if (step + k != 0): # very important
                            steps[jumpto].add(step + k)
        return False

# BFS
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if (not stones): return True
        if (stones[1] != stones[0] + 1): return False # first jump can only be 1
        dest = stones[-1]
        queue = collections.deque()
        queue.append((stones[0] + 1, 1)) # first jump can only be 1
        stones = set(stones)
        visited = set()
        while (queue):
            on, step = queue.popleft()
            if (on == dest): return True
            elif (on > dest): continue
            for k in range(-1, 2):
                jumpto = on + step + k
                if (jumpto in stones and (jumpto, step + k) not in visited):
                    queue.append((jumpto, step + k))
                    visited.add((jumpto, step + k))
        return False

# much slower than the previous two
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if (not stones): return True
        n = len(stones)
        steps = [[False] * n for i in range(n)]
        steps[0][1] = True
        for i in range(1, n):
            for j in range(i):
                dist = stones[i] - stones[j]
                if (dist >= n or not steps[j][dist]): continue
                if (i == n - 1): return True
                for k in range(-1, 2):
                    steps[i][dist + k] = True
        return False
