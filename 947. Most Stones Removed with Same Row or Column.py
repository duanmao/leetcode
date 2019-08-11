# Union Find
# Time: O(n), space: O(n)
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        self.islands = 0
        
        def find(x):
            if (x not in parent):
                parent[x] = x
                self.islands += 1
            if (not x == parent[x]):
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x1, x2):
            px1, px2 = find(x1), find(x2)
            if (not px1 == px2):
                parent[px1] = px2
                self.islands -= 1
                
        for x, y in stones:
            union("row" + str(x), "column" + str(y))
        return len(stones) - self.islands

# DFS
# Time: O(n), space: O(n)
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        coords = set([(x, y) for x, y in stones])
        xtoy, ytox = collections.defaultdict(list), collections.defaultdict(list)
        for x, y in stones:
            xtoy[x].append(y)
            ytox[y].append(x)
            
        def dfs(x, y):
            if ((x, y) in coords):
                coords.discard((x, y))
                for y1 in xtoy[x]:
                    dfs(x, y1)
                for x1 in ytox[y]:
                    dfs(x1, y)
            
        islands = 0
        while (len(coords)):
            x, y = next(iter(coords))
            dfs(x, y)
            islands += 1
        return len(stones) - islands
