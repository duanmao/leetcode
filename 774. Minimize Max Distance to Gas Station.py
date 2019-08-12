# O(n logm), n: len(stations), m: max distance between stations
# space can be O(1), but this implementation is O(n) due to the arrays used for distances
class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        n = len(stations)
        
        def distancePossible(dist):
            need_insert = [int((stations[i] - stations[i - 1]) / dist) for i in range(1, n)]
            return sum(need_insert) <= K
            
        maxdis = max([stations[i] - stations[i - 1] for i in range(1, n)])
        low, high = 0, maxdis
        while (high - low > 1e-6):
            mid = (low + high) / 2
            if (distancePossible(mid)): high = mid
            else: low = mid
        return low

# DP, MLE
# Time: O(nK^2), space: O(nK)
# https://leetcode.com/problems/minimize-max-distance-to-gas-station/solution/
class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        n = len(stations)
        dists = [stations[i] - stations[i - 1] for i in range(1, n)]
        f = [[float('inf')] * (K + 1) for _ in range(n - 1)]
        # f[i][j] = answer for distances[:i+1] when adding j gas stations
        for i in range(K + 1):
            f[0][i] = dists[0] / (i + 1)

        for i in range(1, n - 1):
            for j in range(K + 1):
                for k in range(j + 1):
                    f[i][j] = min(f[i][j], max(dists[i] / (k + 1), f[i - 1][j - k]))

        return f[-1][K]
