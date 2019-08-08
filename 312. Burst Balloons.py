# Time: O(n^3), space: O(n^2)
# https://www.youtube.com/watch?v=IFNibRVgFBo&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=29
# https://leetcode.com/problems/burst-balloons/discuss/?currentPage=1&orderBy=most_votes&query=
# https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if (not nums): return 0
        n = len(nums)
        f = [[0] * n for i in range(n)]
        lastburst = [[-1] * n for i in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                for k in range(i, j + 1):
                    leftaccu = f[i][k - 1] if k - 1 >= i else 0
                    rightaccu = f[k + 1][j] if k + 1 <= j else 0
                    left = nums[i - 1] if i - 1 >= 0 else 1
                    right = nums[j + 1] if j + 1 < n else 1
                    cur = leftaccu + rightaccu + left * right * nums[k]
                    if (cur > f[i][j]):
                        f[i][j] = cur
                        lastburst[i][j] = k
        return f[0][n - 1]
