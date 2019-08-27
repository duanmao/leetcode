# https://leetcode.com/problems/swap-adjacent-in-lr-string/solution/
# https://leetcode.com/articles/swap-adjacent-in-lr-string/
# according to the moving rules, there're 2 invariants always exist as long as the moves are valid
# 1. L and R can never across each other - they must keep exactly the same order relative to each other
# 2. L can never go to the right of its original position, while R can never go left

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

# To demonstrate the above idea clearly: (this implementation takes O(n) space)
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # L and R can never cross each other
        # therefore L and R must have the exactly same relative order
        if (start.replace('X', '') != end.replace('X', '')): return False

        # L can only move left, while R can only move right
        j = 0
        for i, c1 in enumerate(start):
            if (c1 == 'X'): continue
            while (end[j] != c1): j += 1
            if (c1 == 'L' and i < j): return False
            elif (c1 == 'R' and i > j): return False
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
