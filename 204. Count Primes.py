# Time: empirically much much faster than the regular Sieve of Eratosthenes approach
# but I'm not good at analyzing its exact time complexity... :'(
# Detailed explanation: https://leetcode.com/problems/count-primes/discuss/57593/12-ms-Java-solution-modified-from-the-hint-method-beats-99.95/59090
class Solution:
    def countPrimes(self, n: int) -> int:
        if (n < 3):
            return 0
        count = int(n / 2) # half of the numbers are even, thus not prime
        isComposite = [False] * n
        # we're going to find all *odd*, composite numbers to exclude them
        for i in range(3, int(n ** 0.5) + 1, 2): # start from odd and increase by 2
            if (isComposite[i]): # this odd number has already been handled
                continue
            # starting from i * i which is an odd number, we're going to find other
            # *odd* numbers that are multiples of i, that's why the increment is 2 * i
            # since only odd multiples of i are still odd, i.e. i * i, i * (i + 2), ...
            for j in range(i * i, n, 2 * i):
                if (not isComposite[j]):
                    isComposite[j] = True
                    count -= 1
        return count

# Time: O(n log log n), space: O(n)
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes (code in Chinese version)
class Solution:
    def countPrimes(self, n: int) -> int:
        if (n < 3):
            return 0
        isPrime = [True] * n
        for i in range(2, int(n ** 0.5) + 1):
            if (isPrime[i]):
                for j in range(i * i, n, i):
                    isPrime[j] = False
        return sum(isPrime) - 2

class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        for i in range(2, int(n ** 0.5) + 1):
            if (isPrime[i]):
                for j in range(i * i, n, i):
                    isPrime[j] = False
        return len([x for x in range(2, n) if isPrime[x]])

import math
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * (n - 2)
        count = 0
        for i in range(2, n):
            if (isPrime[i - 2]):
                count += 1
                for j in range(i, int(n / i) + 1):
                    if (i * j < n):
                        isPrime[i * j - 2] = False
                    else:
                        break
        return count
