# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108871/2-solutions-2-states-DP-solutions-clear-explanation!
# Time: O(n), space: O(n)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if (not prices): return 0
        n = len(prices)
        # buy[i]: the max profit at day i in buy state: the last action we took is 
        # buying the stock at day k, where k <= i. 
        # so we can either sell the stock at day i+1, or do nothing.
        # thus it comes from a previous buy state, or a previous sell state with a buy-in at day i
        # base case: buy in at day 0
        buy = [-prices[0]] + [0] * (n - 1)
        # sell[i]: the max profit at day i in sell state: the last action we took is 
        # selling the stock at day k, where k <= i. 
        # so we can either buy the stock at day i + 1, or do nothing.
        # thus it comes from a previous sell state, or a previous buy state with a sell at day i
        # base case: 0 at day 0 since we have nothing to sell
        sell = [0] * n
        # the transaction fee can be applied at either a buy-in or a sell
        for i, price in enumerate(prices):
            if (i == 0): continue # day 0 is the base cases, so must start from day 1
            buy[i] = max(buy[i - 1], sell[i - 1] - price)
            sell[i] = max(sell[i - 1], buy[i - 1] + price - fee)
        return sell[n - 1]

# observing that we actually only need buy[i - 1] and sell[i - 1] at any particular day i, thus we
# can eliminate the two arrays to two variables which store the previous state we need, so as to cut
# the space complexity to O(1)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if (not prices): return 0
        n = len(prices)
        # buy[i]: the max profit at day i in buy state: the last action we took is
        # buying the stock at day k, where k <= i.
        # so we can either sell the stock at day i+1, or do nothing.
        # thus it comes from a previous buy state, or a previous sell state with a buy-in at day i
        # base case: buy in at day 0
        buy = -prices[0]
        # sell[i]: the max profit at day i in sell state: the last action we took is
        # selling the stock at day k, where k <= i.
        # so we can either buy the stock at day i + 1, or do nothing.
        # thus it comes from a previous sell state, or a previous buy state with a sell at day i
        # base case: 0 at day 0 since we have nothing to sell
        sell = 0
        # the transaction fee can be applied at either a buy-in or a sell
        for i, price in enumerate(prices):
            if (i == 0): continue # day 0 is the base cases, so must start from day 1
            buy = max(buy, sell - price)
            # we don't have to record the previous buy before we change it above, at day i,
            # since a sell immediately after a buy-in in the same day can never do better
            # than doing nothing, because of the transaction fee
            sell = max(sell, buy + price - fee)
        return sell


# a more interesting but occult solution (which I haven't been able to understood until now)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/201603/Python.-Greedy-is-good.
