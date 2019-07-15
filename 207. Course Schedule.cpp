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
