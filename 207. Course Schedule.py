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
        def Circle(courses, cur, visited):
            if (visited[cur] == 1):
                # visited along the path
                return True
            if (visited[cur] == 2):
                # Has been visited before for other paths
                return False
            visited[cur] = 1
            for i in courses[cur]:
                if (Circle(courses, i, visited)):
                    return True
            visited[cur] = 2
            return False
        
        dict = [[] for i in range(numCourses)] 
        for course, pre in prerequisites:
            dict[course].append(pre)

        visited = [0] * numCourses
        for i, pres in enumerate(dict):
            if (len(pres)):
                if (not visited[i] and Circle(dict, i, visited)):
                    return False
                
        return True
