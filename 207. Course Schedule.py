# BFS
# Topological sort
# Time: O(v + e), space: O(v + e)
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque()
        count = 0
        for v, indg in enumerate(indegree):
            if indg == 0: queue.append(v)
        while queue:
            cur = queue.popleft()
            count += 1
            for v in graph[cur]:
                indegree[v] -= 1
                if indegree[v] == 0: queue.append(v)
        return count == numCourses

# DFS
# Time: O(v + e), space: O(v + e)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
        visited = [0] * numCourses

        def hasCycle(cur):
            if visited[cur] == 2: # visited
                return False
            elif visited[cur] == 1: # visiting
                return True
            visited[cur] = 1
            for v in graph[cur]:
                if hasCycle(v): return True
            visited[cur] = 2
            return False

        for v in range(numCourses):
            if hasCycle(v): return False
        return True
