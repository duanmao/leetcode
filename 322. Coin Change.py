# DP - bottom up
# a more natural bottom-up DP solution
# f(S): minimum number of coins needed to make up amount S using given coin denominations
# thus, f(S) = min(f(S - ci)) + 1
# the first one below iterates coins first, so that the second loop will start directly from
# the current coin's denomination and skip all smaller amounts, which makes it faster than the
# second version
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [float('inf')] * (amount + 1)
        f[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                if (i - coin >= 0 and f[i - coin] < float('inf')):
                    f[i] = min(f[i], f[i - coin] + 1)
        return f[amount] if f[amount] < float('inf') else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [float('inf')] * (amount + 1)
        f[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if (i - coin >= 0 and f[i - coin] < float('inf')):
                    f[i] = min(f[i], f[i - coin] + 1)
        return f[amount] if f[amount] < float('inf') else -1

# DP - top down
# f(S): minimum number of coins needed to make up amount S using given coin denominations
# thus, f(S) = min(f(S - ci)) + 1
# Time: O(S*n) where S is the target amount and n is the denomination count
# In the worst case the recursive tree of the algorithm has height of S,
# i.e. the algorithm solves only S subproblems because it caches precalculated solutions in a table.
# Each subproblem is computed with n iterations, one by coin denomination. Therefore time complexity O(S*n)
# Space: O(S)
# The difference between this one and the brute force is that the visited sub-amount will not be
# compute again, and its result is cached in the table so that can be returned directly.
# Thus, distinguishing unvisited amounts from the visited ones is crucial, especially the visited
# but cannot-solved ones, they must not be confused with the unvisited ones.
# As a result, we basically need 3 flags to differentiate them:
# float_MAX for unvisited amounts; non-negatives for solved amounts; -1 for other tried amounts.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def makeup(f, target):
            if (target < 0): # visited and no solution found
                return -1
            if (f[target] < float('inf')): # visited and solved
                return f[target]
            minUse = float('inf')
            for coin in coins:
                res = makeup(f, target - coin)
                if (res != -1):
                    assert(f[target - coin] == res)
                    minUse = min(minUse, res + 1)
            f[target] = minUse if minUse < float('inf') else -1
            return f[target]
            
        f = [float('inf')] * (amount + 1) # using MAX to mark unvisited
        f[0] = 0
        makeup(f, amount)
        return f[amount]

# Brute force - DFS with pruning
# Although this solution is a pure DFS which can be considered as a brute force search, it is
# *AMAZINGLY* fast and beats nearly all other solutions (96%) in time on LeetCode OJ.
class Solution:
    def coinChange(self, coins, amount):
        coins.sort(reverse = True) # absolutely indispensable!!!
        self.minUse = float('inf')

        def dfs(possibleStart, target, currentUse):
            if not target:
                self.minUse = min(self.minUse, currentUse)
            for i in range(possibleStart, len(coins)):
                if coins[i] <= target < coins[i] * (self.minUse - currentUse): # if hope still exists
                    dfs(i, target - coins[i], currentUse + 1)

        for i in range(len(coins)):
            dfs(i, amount, 0)
        return self.minUse if self.minUse < float('inf') else -1

# BFS
# Also beats most solutions (92%+) on LeetCode OJ in time, but slightly slower than the previous one
# But the most weird thing is, unlike common BFS using queue, arrays must be used here
# otherwise TLE. I'm guessing it's because the operations on a queue is slower than operating on an
# array here, but it's not verified except on LeetCode OJ.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if (not amount):
            return 0
        last, cur = [0], []
        visited = [True] + [False] * amount
        used = 0
        while (last):
            used += 1
            for v in last:
                for coin in coins:
                    s = coin + v
                    if (s == amount):
                        return used
                    elif (s < amount and not visited[s]):
                        cur.append(s)
                        visited[s] = True
            last, cur = cur, []
        return -1

# Brute force - DFS without optimization
# Time: O(S^n) where S is the target amount and n is the number of given coin denominations
# because every coin denomination ci could have at most S/ci values (frequencies)
# i.e. it can be chosen at most S/ci times
# space complexity: O(S) since the maximum depth of recursion is S
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def coinCombs(coins, amount):
            if (amount == 0):
                return 0
            elif (amount < 0):
                return -1
            minUse = float('inf')
            for coin in coins:
                use = coinCombs(coins, amount - coin)
                if (use >= 0):
                    minUse = min(minUse, use + 1)
            return minUse if minUse < float('inf') else -1
                
        return coinCombs(coins, amount)
