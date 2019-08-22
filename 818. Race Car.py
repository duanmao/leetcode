# Time: O(TlogT) since each target i does (log i) work, space: O(T)
class Solution:
    def racecar(self, target: int) -> int:
        def distance(k):
            # running distance with k accelerations
            return 2 ** k - 1
        
        # f[i]: the shortest length of instructions to reach i
        f = [0] + [float('inf')] * target
        for i in range(1, target + 1):
            k = i.bit_length()
            if (distance(k) == i):
                f[i] = k
            else:
                # accelerate for k times, reverse, and accelerate to target i
                f[i] = k + 1 + f[distance(k) - i]
                # accelerate for k - 1 times, reverse to go back with
                # acceleration for j times, reverse, accelerate to target i
                for j in range(k - 1):
                    f[i] = min(f[i], k - 1 + j + 2 + f[i - (distance(k - 1) - distance(j))])
        return f[target]
