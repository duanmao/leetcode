# O(n + p), n: len(words), p: len(pairs)
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        parent = {}
        
        def find(x):
            if (x not in parent): parent[x] = x
            if (parent[x] == x): return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x1, x2):
            p1, p2 = find(x1), find(x2)
            parent[p1] = p2
        
        if (len(words1) != len(words2)): return False
        for p1, p2 in pairs:
            union(p1, p2)
        for w1, w2 in zip(words1, words2):
            if (find(w1) != find(w2)): return False
        return True
