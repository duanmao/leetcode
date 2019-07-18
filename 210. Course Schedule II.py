# Time: O(V+E), space: O(V+E)
# explanation: https://leetcode.com/problems/course-schedule-ii/discuss/59317/Two-AC-solution-in-Java-using-BFS-and-DFS-with-explanation
import Queue
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for i in range(numCourses)]
        inDegree = [0] * numCourses
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            inDegree[crs] += 1
        
        order = []
        queue = Queue.Queue()
        for i, ind in enumerate(inDegree):
            if (ind == 0): # root
                queue.put(i)
        while (not queue.empty()):
            cur = queue.get()
            order.append(cur)
            for nxt in graph[cur]:
                inDegree[nxt] -= 1
                if (inDegree[nxt] == 0):
                    queue.put(nxt)
        return order if len(order) == numCourses else []
