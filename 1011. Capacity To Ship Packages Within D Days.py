# Time: O(nlog(sum(weights)), space: O(1)
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def shipdays(maxcapc):
            days = 1
            capc = 0
            for w in weights:
                capc += w
                if (capc > maxcapc):
                    days += 1
                    capc = w
            return days
        
        low, high = max(weights), sum(weights)
        while (low <= high):
            mid = (low + high) // 2
            days = shipdays(mid)
            if (days <= D): high = mid - 1
            else: low = mid + 1
        return low

# same as Q410, could use DP but TLE for this case, O(D*n^2), D: days, n: len(weights)
# f[i][j]: the min capacity to ship 1-i packages within j days
# f[i][j] = min(max(f[k][j - 1], sum(weights[k+1:j])) for 0 <= k < i
# initialization: f[len(weights) + 1][day + 1]
# f[i][0] = MAX, f[0][j] = 0
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/258558/JAVA-DP-and-binary-search
