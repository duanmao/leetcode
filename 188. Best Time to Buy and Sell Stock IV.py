# Time: O(n + k logn), space: O(n) 
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54118/C%2B%2B-Solution-with-O(n-%2B-klgn)-time-using-Max-Heap-
# it's crazy... crazy... crazy...
from heapq import *
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        profits = [] # max heap
        stack = []
        valley = peak = -1
        while (peak < n):
            # find the next valley to peak interval
            valley = peak + 1
            while (valley < n - 1 and prices[valley] >= prices[valley + 1]): valley += 1
            peak = valley + 1
            while (peak < n - 1 and prices[peak] <= prices[peak + 1]): peak += 1
            
            if (peak >= n): break # IMPORTANT safety check in this implementation
            
            # for all the valleys detected before, if they're larger than the current one,
            # the best we can do with them is to use them directly with their coming peaks,
            # so store these best profits we can get from them to the heap
            while (stack and prices[stack[-1][0]] >= prices[valley]):
                v, p = stack.pop()
                heappush(profits, -(prices[p] - prices[v]))
            
            # all higher valleys have been popped out, the left ones are lower valleys.
            # with them, if their corresponding peaks are lower than the current one,
            # we will have two options: 1. do two transactions separately; Or,
            # 2. do only one transaction that buys in at the previous valley, and
            # sells out at the current peak. 
            # both scenarios should be stored in the heap, and for this time, we will store
            # the "extra" profit that we can get with two separate transactions, and leave
            # the profit from only one transaction in the stack to process later
            # namely, we have v1, p1 and v2, p2 where v1 < v2 and p1 < p2
            # with two transactions, we get p1 - v1 + p2 - v2
            # with one transaction, the max profit we get is p2 - v1
            # the difference between them is p1 - v2, which is what we're storing here
            # and record v1 for the one transaction scenario and keep it in the stack as regular
            while (stack and prices[stack[-1][1]] <= prices[peak]):
                v, p = stack.pop()
                heappush(profits, -(prices[p] - prices[valley]))
                valley = v
            
            # save valley and peak pair into stack
            stack.append((valley, peak))
        
        # process (valley, peak) pairs left in stack for their profits, same as above
        while (stack):
            valley, peak = stack.pop()
            heappush(profits, -(prices[peak] - prices[valley]))
            
        maxprof = 0
        for i in range(k):
            if (profits): maxprof += -heappop(profits)
            else: break
        return maxprof

# DP: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54113/a-concise-dp-solution-in-java
# Time: O(nk), space: O(k)
# however I cannot clearly fathom why my implementation below works... sigh
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if (not prices): return 0
        n = len(prices)
        if (k >= n // 2):
            buy, sell = -prices[0], 0
            for i, price in enumerate(prices):
                buy = max(buy, sell - price)
                sell = max(sell, buy + price)
            return sell

        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)
        for i, price in enumerate(prices):
            for t in range(1, k + 1): # transactions loop must be the inside loop in this implementation
                buy[t] = max(buy[t], sell[t - 1] - price)
                sell[t] = max(sell[t], buy[t] + price)
        print(buy, sell)
        return sell[k]

# Time: O(nk), space: O(nk)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54113/A-Concise-DP-Solution-in-Java
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
