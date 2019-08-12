# https://leetcode.com/problems/swap-adjacent-in-lr-string/solution/
# https://leetcode.com/articles/swap-adjacent-in-lr-string/
# Time: O(n), space: O(1)
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i = j = 0
        m, n = len(start), len(end)
        while (i < m or j < n):
            while (i < m and start[i] == 'X'): i += 1
            while (j < n and end[j] == 'X'): j += 1
            if (i == m and j == n): return True
            elif (i == m or j == n): return False
            if (start[i] != end[j]): return False
            if (start[i] == 'L' and i < j): return False
            if (start[i] == 'R' and i > j): return False
            i += 1
            j += 1
        return True

# Time: O(n), space: O(n)
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace('X','') != end.replace('X', ''):
            return False
        
        def indices(s):
            ind = []
            for i, c in enumerate(s):
                if (c == 'L'): ind.append(-i)
                elif (c == 'R'): ind.append(i)
            return ind
        
        return all(x1 >= x2 for x1, x2 in zip(indices(end),indices(start)))
