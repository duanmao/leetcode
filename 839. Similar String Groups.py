# Union Find
# Time: O(n^2 * l), space: O(n)
# though this implementation in python cannot AC on leetcode, always TLE
# but exactly the same strategy passes in C++
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:

        # w1 and w2 are already anagrams
        def similar(w1, w2):
            if (w1 == w2): return True
            if (len(w1) != len(w2)): return False
            diffs = []
            for i in range(len(w1)):
                if (w1[i] != w2[i]): diffs.append(i)
                if (len(diffs) > 2): return False
            i, j = diffs
            return [w1[i], w1[j]] == [w2[j], w2[i]]

        parent = {}
        self.group = len(A)

        def find(x):
            if (x not in parent): parent[x] = x
            if (parent[x] != x):
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootx, rooty = find(x), find(y)
            if (rootx != rooty):
                self.group -= 1
                parent[rootx] = rooty

        for i, w in enumerate(A):
            for j in range(i + 1, len(A)):
                if (similar(w, A[j])):
                    union(i, j)
        return self.group
