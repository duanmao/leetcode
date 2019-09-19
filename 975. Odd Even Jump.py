# Time: O(nlogn), space: O(n)
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        # toHigher[i] = j means from pos i we can jump to pos j with odd jump
        # toLower[i] = j means from pos i we can jump to pos j with even jump
        toHigher, toLower = [-1] * n, [-1] * n
        # monotonic stack
        stack = []
        # visit (A[i], i) in ascending order so that for every previously visited element
        # (A[p], p), as long as p < i, we know that we will jump from p to i with odd jump
        for a, i in sorted([(a, i) for i, a in enumerate(A)]):
            while stack and stack[-1] < i:
                toHigher[stack.pop()] = i
            stack.append(i)
        stack = []
        # do the same for even jumps to get toLower, namely:
        # visit (A[i], i) in A[i]'s descending order so that for every previously visited element
        # (A[p], p), as long as p < i, we know that we will jump from p to i with even jump
        # but note that we need to break tie when multiple positions behind sharing the same value,
        # we can only jump to the nearest pos at this time, so essentially we want array [(A[i], i)]
        # descends w.r.t. A[i] but ascends w.r.t. i to break tie, so we use the trick of sorting
        # [(-A[i], i)] in ascending order for this, instead of sorting [(A[i], i)] in descending order
        for a, i in sorted([(-a, i) for i, a in enumerate(A)]):
            while stack and stack[-1] < i:
                toLower[stack.pop()] = i
            stack.append(i)

        # DP
        # jump*er[i]: whether the end can be reached with an odd/even jump from i
        jumpHigher, jumpLower = [False] * (n - 1) + [True], [False] * (n - 1) + [True]
        for i in range(n - 2, -1, -1):
            jumpHigher[i] = toHigher[i] != -1 and jumpLower[toHigher[i]]
            jumpLower[i] = toLower[i] != -1 and jumpHigher[toLower[i]]
        return sum(jumpHigher) # always start with odd (1) jump


class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        nextHigher, nextLower = [-1] * n, [-1] * n
        stack = []
        for a, i in sorted([(A[i], i) for i in range(n)]):
            while (len(stack) and stack[-1] < i):
                nextHigher[stack.pop()] = i
            stack.append(i)
        stack = []
        for a, i in sorted([(-A[i], i) for i in range(n)]):
            while (len(stack) and stack[-1] < i):
                nextLower[stack.pop()] = i
            stack.append(i)
            
        toHigher = [False] * (n - 1) + [True] # odd-th jumps
        toLower = [False] * (n - 1) + [True] # even-th jumps
        for i in range(n - 1)[::-1]:
            toHigher[i] = not nextHigher[i] == -1 and toLower[nextHigher[i]]
            toLower[i] = not nextLower[i] == -1 and toHigher[nextLower[i]]
        return sum(toHigher)


# Time: O(n^2), space: O(n)
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        if (not n): return 0
        f = [[False, False] for i in range(n - 1)] + [[True, True]]
        for i in range(n - 1)[::-1]:
            oddreach = evenreach = -1
            for j in range(i + 1, n):
                if (A[i] <= A[j]):
                    if (oddreach == -1 or A[j] < A[oddreach]):
                        oddreach = j
                if (A[i] >= A[j]):
                    if (evenreach == -1 or A[j] > A[evenreach]):
                        evenreach = j
            f[i][1] = not oddreach == -1 and f[oddreach][0]
            f[i][0] = not evenreach == -1 and f[evenreach][1]
        return sum([odd for even, odd in f])
