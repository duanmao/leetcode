# basic DP solution is the same as the solution to
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
# for detailed explanation, refer to the solution of Q714
# Time: O(n), space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (not prices): return 0
        n = len(prices)
        buy = [-prices[0]] + [0] * (n - 1)
        sell = [0] * n
        for i, price in enumerate(prices):
            if (i == 0): continue
            buy[i] = max(buy[i - 1], (sell[i - 2] if i > 1 else 0) - price)
            sell[i] = max(sell[i - 1], buy[i - 1] + price)
        return sell[n - 1]

# Likewise, same as Q714, the space complexity can be reduced to O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (not prices): return 0
        n = len(prices)
        buy = -prices[0]
        sell = cooldownsell = 0
        for i, price in enumerate(prices):
            if (i == 0): continue
            buy = max(buy, cooldownsell - price)
            cooldownsell = sell
            sell = max(sell, buy + price)
        return sell
