# Time: O(n), space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = -1
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1] and buy == -1:
                buy = i
            elif prices[i] > prices[i + 1] and buy != -1:
                profit += prices[i] - prices[buy]
                buy = -1
        if buy != -1: profit += prices[-1] - prices[buy] # don't forget
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (not prices): return 0
        buy = -prices[0]
        sell = 0
        for i, price in enumerate(prices):
            buy = max(buy, sell - price)
            sell = max(sell, buy + price)
        return sell
