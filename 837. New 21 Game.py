# DP top-down
# p[i]: the probability of getting i points
# i points can only be got based on [i - W, i - 1] points, with drawing another card of [1, W]
# points with probability 1/W, thus p[i] = sum(p[i-W:i-1]) / W
# Time: O(N), space: O(N)
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        p = [1] + [0] * N
        prob = 0
        for i in range(1, N + 1):
            if (i - 1 < K): prob += p[i - 1] # cards are drawn only if we have less than K
            if (i > W): prob -= p[i - W - 1] # prob is the sum of the previous window of length W
            p[i] = prob / W
        return sum(p[K:N + 1])

# TLE but most straightforward. DP bottom-up
# p[i]: the probability of getting i points
# thus when we already have i points and i < K, we need to draw another round, which can yield a
# point number j within [1, W] with probability 1/W, so that we get i + j points now
# Time: O(KW), space: O(K+W)
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        p = [1] + [0] * (K + W - 1)
        for i in range(K):
            for j in range(1, W + 1):
                p[i + j] += (p[i] * 1/W)
        return sum(p[K:N+1])
