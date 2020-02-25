# Time: O(n^2), space: O(n^2)
# Union-Find
# https://leetcode.com/problems/regions-cut-by-slashes/discuss/205680/JavaC%2B%2BPython-Split-4-parts-and-Union-Fine
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        parents = {}
        
        def find(x):
            if x not in parents: parents[x] = x
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py: parents[px] = py
                
        # cut a grid into 4 parts:
        #  \ 0 /
        #   \ / 1
        # 3 / \
        #  / 2 \
        
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i: union((i, j, 0), (i - 1, j, 2))
                if j: union((i, j, 3), (i, j - 1, 1))
                if grid[i][j] in {'/', ' '} :
                    union((i, j, 0), (i, j, 3))
                    union((i, j, 1), (i, j, 2))
                if grid[i][j] in {'\\', ' '} :
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 2), (i, j, 3))
        # map(find, parents) will find all independent roots of all members
        # as our target is the total number of separated unions,
        # the number of unique roots is the final answer
        return len(set(map(find, parents)))

# DFS
# Time & space: O(n ^ 2)
# https://leetcode.com/problems/regions-cut-by-slashes/discuss/207045/Python-straightforward-O(N)-DFS-~100-ms-beats-100
# empirically much faster
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)

        # cut a grid into 4 parts:
        #  \ 0 /
        #   \ / 1
        # 3 / \
        #  / 2 \
        label = [[[0] * 4 for j in range(n)] for i in range(n)]

        def dfs(row, col, part, region):
            if (row < 0 or row >= n or col < 0 or col >= n or
                label[row][col][part]): return
            if grid[row][col] in {'/', ' '}:
                if 1 <= part <= 2 or grid[row][col] == ' ':
                    label[row][col][1] = label[row][col][2] = region
                    # extend to neighbors
                    dfs(row, col + 1, 3, region) # part 1 connects to right 3
                    dfs(row + 1, col, 0, region) # part 2 connects to 0 below
                if part in {0, 3} or grid[row][col] == ' ':
                    label[row][col][0] = label[row][col][3] = region
                    dfs(row - 1, col, 2, region) # part 0
                    dfs(row, col - 1, 1, region) # part 3
            if grid[row][col] in {'\\', ' '}:
                if part <= 1 or grid[row][col] == ' ':
                    label[row][col][0] = label[row][col][1] = region
                    # extend to neighbors
                    dfs(row - 1, col, 2, region) # part 0
                    dfs(row, col + 1, 3, region) # part 1
                if 2 <= part <= 3 or grid[row][col] == ' ':
                    label[row][col][2] = label[row][col][3] = region
                    dfs(row + 1, col, 0, region) # part 2
                    dfs(row, col - 1, 1, region) # part 3

        region = 0
        for i in range(n):
            for j in range(n):
                # dfs for each part (extend current region)
                for k in range(4):
                    if not label[i][j][k]:
                        region += 1
                        dfs(i, j, k, region)
        return region
