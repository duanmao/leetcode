class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        profit = 0
        for p in prices:
            minprice = min(minprice, p)
            profit = max(profit, p - minprice)
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (not prices): return 0
        pro = maxpro = 0
        for i in range(1, len(prices)):
            pro += prices[i] - prices[i - 1]
            pro = max(pro, 0)
            maxpro = max(maxpro, pro)
        return maxpro
