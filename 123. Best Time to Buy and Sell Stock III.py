# Time: O(n), space: O(1)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/149383/Easy-DP-solution-using-state-machine-O(n)-time-complexity-O(1)-space-complexity
# ... https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39611/Is-it-Best-Solution-with-O(n)-O(1).
# It's... crazy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        balance_bought_1 = balance_bought_2 = float('-inf')
        balance_sold_1 = balance_sold_2 = 0
        for price in prices:
            balance_bought_1 = max(balance_bought_1, -price)
            balance_sold_1 = max(balance_sold_1, price + balance_bought_1)
            balance_bought_2 = max(balance_bought_2, balance_sold_1 - price)
            balance_sold_2 = max(balance_sold_2, price + balance_bought_2)
        return balance_sold_2

# Time: O(n), space: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (not prices): return 0
        n = len(prices)
        first = [0] * n
        minprice = prices[0]
        for i in range(1, n):
            first[i] = max(first[i - 1], prices[i] - minprice)
            minprice = min(minprice, prices[i])
        maxprice = prices[n - 1]
        maxpro = second = 0
        for i in range(0, n - 1)[::-1]:
            second = max(second, maxprice - prices[i])
            maxpro = max(maxpro, first[i] + second)
            maxprice = max(maxprice, prices[i])
        return maxpro
