# DP
# https://leetcode.com/problems/optimal-account-balancing/discuss/219187/Short-O(N-*-2N)-DP-solution-with-detailed-explanation-and-complexity-analysis
# Time: O(n * 2^n), space: O(2^n)
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        debt = collections.defaultdict(int)
        for lender, borrower, amount in transactions:
            debt[borrower] += amount
            debt[lender] -= amount
        debts = [debt[p] for p in debt if debt[p]]

        # in essence, we want to find the max number of subsets of debts that
        # the subset sum is zero, so that we'll arrive at the minimum number
        # of transactions as: n - (max number of subsets)
        n = len(debts)
        totalStates = 2 ** n
        # zerosets[state]: the max # of zero sets (set elements sum up to zero)
        # that can be formed by the elements in state
        zerosets = [0] * totalStates
        # sums[state]: sum of this state
        sums = [0] * totalStates

        for state in range(totalStates):
            for i in range(n):
                if (state & (1 << i)): continue # i-th element is already included
                nextstate = state ^ (1 << i) # mark i-th element as included
                sums[nextstate] = sums[state] + debts[i]
                if (sums[nextstate] == 0):
                    zerosets[nextstate] = max(zerosets[nextstate], zerosets[state] + 1)
                else:
                    zerosets[nextstate] = max(zerosets[nextstate], zerosets[state])

        return n - zerosets[totalStates - 1]

# https://leetcode.com/problems/optimal-account-balancing/discuss/130895/Recursion-Logical-Thinking
# basically a subset sum problem, NP-complete https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
# Time: worst case should be O(n!)
# https://leetcode.com/problems/optimal-account-balancing/discuss/95355/11-liner-9ms-DFS-solution-(detailed-explanation)/99754
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        def settle(debts, cur):
            while (cur < len(debts) and not debts[cur]): cur += 1
            if (cur == len(debts)): return 0

            # try greedy pruning
            for i in range(cur + 1, len(debts)):
                if (debts[i] == -debts[cur]):
                    debts[i] = 0
                    mintrans = 1 + settle(debts, cur + 1)
                    debts[i] = -debts[cur]
                    return mintrans

            mintrans = float('inf')
            seen = set() # very important optimization, otherwise TLE (without the above pruning)
            for i in range(cur + 1, len(debts)):
                if (debts[i] not in seen and debts[cur] * debts[i] < 0):
                    debts[i] += debts[cur]
                    mintrans = min(mintrans, 1 + settle(debts, cur + 1))
                    debts[i] -= debts[cur]
                    seen.add(debts[i])
            return mintrans

        debt = collections.defaultdict(int)
        for lender, borrower, amount in transactions:
            debt[borrower] += amount
            debt[lender] -= amount
        debts = [debt[p] for p in debt if debt[p]]

        return settle(debts, 0)

# basically the same idea, but more straightforward than above IMO.. though slower
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        def settle(debt):
            for person in debt:
                if (debt[person]):
                    mintrans = float('inf')
                    amount = debt[person]
                    debt[person] = 0
                    seen = set() # very important optimization, otherwise TLE
                    for other in debt:
                        if (debt[other] not in seen and amount * debt[other] < 0):
                            debt[other] += amount
                            mintrans = min(mintrans, 1 + settle(debt))
                            debt[other] -= amount
                            seen.add(debt[other])
                    debt[person] = amount
                    return mintrans
            return 0

        debt = collections.defaultdict(int)
        for lender, borrower, amount in transactions:
            debt[borrower] += amount
            debt[lender] -= amount

        return settle(debt)
