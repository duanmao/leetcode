# LIS
# Time: O(nlogn), space: O(maxRoll)
# key point: sort envelopes ascending on width but descending on height when widths are same
# https://leetcode.com/problems/russian-doll-envelopes/discuss/82763/Java-NLogN-Solution-with-Explanation
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if (not envelopes): return 0
        envelopes.sort(key = lambda env: (env[0], -env[1]))
        outerH = []
        
        def checkEnv(h):
            low, high = 0, len(outerH) - 1
            while (low <= high):
                mid = (low + high) // 2
                if (outerH[mid] < h):
                    low = mid + 1
                else:
                    high = mid - 1
            return low
            
        for w, h in envelopes:
            replace = checkEnv(h)
            if (replace >= len(outerH)):
                outerH.append(h)
            else:
                outerH[replace] = h
        return len(outerH)

# DP - TLE
# Time: O(n^2), space: O(n)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if (not envelopes): return 0
        n = len(envelopes)
        envelopes.sort()
        # f[i]: the max russian doll includes the i-th envelope
        f = [1]* n
        for i in range(1, n):
            wi, hi = envelopes[i]
            for j in range(i):
                wj, hj = envelopes[j]
                if (wi > wj and hi > hj):
                    f[i] = max(f[i], f[j] + 1)
        return max(f)
