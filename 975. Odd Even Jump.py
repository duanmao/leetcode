# Time: O(nlogn), space: O(n)
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
