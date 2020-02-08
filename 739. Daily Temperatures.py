# Time: O(n), space: O(n)
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        s = []
        res = [0] * n
        for i, t in enumerate(T):
            while s and s[-1][1] < t:
                ind, temp = s.pop()
                res[ind] = i - ind
            s.append((i, t))
                
        return res

# Time: O(n) (though don't know how to prove), space: O(1)
# https://leetcode.com/problems/daily-temperatures/discuss/121787/C%2B%2B-Clean-code-with-explanation%3A-O(n)-time-and-O(1)-space-(beats-99.13)
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        res = [0] * n
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and T[j] <= T[i] and res[j] != 0:
                j = j + res[j]
            if j < n and T[j] > T[i]: res[i] = j - i
        return res
