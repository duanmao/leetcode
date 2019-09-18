# Time: O(n), space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought = -1
        profit = 0
        for i, price in enumerate(prices):
            if (i < len(prices) - 1 and prices[i] < prices[i + 1]):
                if (bought == -1 or prices[i] < prices[bought]):
                    bought = i
            elif (i == len(prices) - 1 or prices[i] > prices[i + 1]):
                if (bought != -1):
                    profit += prices[i] - prices[bought]
                    bought = -1
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
