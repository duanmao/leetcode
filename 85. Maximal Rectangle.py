# Time: O(mn), space: O(n)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def maxRecArea(hist):
            stack = []
            maxarea = 0
            for i, h in enumerate(hist):
                leftmost = i
                while (stack and stack[-1][0] >= h):
                    height, leftmost = stack.pop()
                    maxarea = max(maxarea, height * (i - leftmost))
                stack.append((h, leftmost))
            n = len(hist)
            while stack:
                height, leftmost = stack.pop()
                maxarea = max(maxarea, height * (n - leftmost))
            return maxarea
        
        if (not matrix): return 0
        m, n = len(matrix), len(matrix[0])
        hist = [0] * n
        maxrec = 0
        for i in range(m):
            for j in range(n):
                if (matrix[i][j] == '1'): hist[j] += 1
                else: hist[j] = 0
            maxrec = max(maxrec, maxRecArea(hist))
        return maxrec
