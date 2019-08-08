# Time: O(nk), space: O(nk)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54113/A-Concise-DP-Solution-in-Java
# much more fancy O(n) approach which I haven't looked at:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54118/C%2B%2B-Solution-with-O(n-%2B-klgn)-time-using-Max-Heap-and-Stack
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54145/O(n)-time-8ms-Accepted-Solution-with-Detailed-Explanation-(C%2B%2B)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if (not prices): return 0
        n = len(prices)
        maxpro = 0
        
        if (k > n // 2): # more transactions are allowed than the most we can complete
            # so just solve it O(n) directly, as if unlimited transactions are permitted
            # in essence https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
            buy = -1
            for i in range(n):
                if (i < n - 1 and prices[i] < prices[i + 1]):
                    if (buy == -1):
                        buy = i
                elif (not buy == -1):
                    maxpro += (prices[i] - prices[buy])
                    buy = -1
            return maxpro
        
        f = [[0] * (k + 1) for i in range(n)]
        for j in range(1, k + 1):
            # the max profit made with completing at most j - 1 transactions and then
            # buying one more stock back during the days [0, i - 1], so that we can
            # sell the stock to complete the j-th transaction on day i
            maxProf_j_1 = -prices[0]
            for i in range(1, n):
                f[i][j] = max(f[i - 1][j], maxProf_j_1 + prices[i])
                maxProf_j_1 = max(maxProf_j_1, f[i - 1][j - 1] - prices[i])
        return f[n - 1][k]
