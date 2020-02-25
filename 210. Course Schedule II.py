# Time: O(V+E), space: O(V+E)
# explanation: https://leetcode.com/problems/course-schedule-ii/discuss/59317/Two-AC-solution-in-Java-using-BFS-and-DFS-with-explanation
# topological sort
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        queue = collections.deque()
        for c, ind in enumerate(indegree):
            if ind == 0: queue.append(c)
        order = []
        while queue:
            c = queue.popleft()
            order.append(c)
            for nb in graph[c]:
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    queue.append(nb)
        return order if len(order) == numCourses else []
