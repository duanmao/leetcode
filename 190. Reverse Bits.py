# explanation: https://leetcode.com/problems/reverse-bits/discuss/54738/Sharing-my-2ms-Java-Solution-with-Explanation
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rvs = 0
        for i in range(32):
            rvs <<= 1
            rvs += 1 if (n & 1) % 2 else 0
            n >>= 1
        return rvs
