class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (not prices): return 0
        minprice = prices[0]
        maxpro = 0
        for pr in prices:
            minprice = min(minprice, pr)
            maxpro = max(maxpro, pr - minprice)
        return maxpro

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (not prices): return 0
        pro = maxpro = 0
        for i in range(1, len(prices)):
            pro += prices[i] - prices[i - 1]
            pro = max(pro, 0)
            maxpro = max(maxpro, pro)
        return maxpro
