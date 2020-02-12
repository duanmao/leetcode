from collections import deque

# Time: O(mn), space: O(mn)
# BFS, or DFS will do as well
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image: return image
        ori = image[sr][sc]
        if ori == newColor: return image
        m, n = len(image), len(image[0])
        direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        q.append((sr, sc))
        image[sr][sc] = newColor
        while q:
            r, c = q.popleft()
            for mr, mc in direc:
                nr, nc = r + mr, c + mc
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == ori: 
                    q.append((nr, nc))  
                    image[nr][nc] = newColor
        return image
