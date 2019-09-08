# Time: O(n), space: O(1)

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        at = 0
        # walk up
        while (at < n - 1 and A[at] < A[at + 1]): at += 1
        # reach peak
        if (at == 0 or at == n - 1): return False
        # walk down
        while (at < n - 1 and A[at] > A[at + 1]): at += 1
        return at == n - 1

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if (len(A) < 3): return False
        up = down = None
        for i in range(1, len(A)):
            if down and A[i - 1] <= A[i]: return False
            if A[i - 1] < A[i]: up = True
            elif A[i - 1] > A[i]: down = True
        return up and down
