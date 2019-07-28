# Time: O(n), space: O(1)
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        prev = 1
        prev2 = 0
        for i in range(n):
            cur = 0
            if (not s[i] == '0'): cur = prev
            if (i and (s[i - 1] == '1' or (s[i - 1] == '2' and ord(s[i]) <= ord('6')))):
                cur += prev2
            prev2 = prev
            prev = cur
        return prev

# Time: O(n), space: O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(1, n + 1):
            if (not s[i - 1] == '0'): f[i] = f[i - 1]
            if (i > 1 and (s[i - 2] == '1' or (s[i - 2] == '2' and ord(s[i - 1]) <= ord('6')))):
                f[i] += f[i - 2]
        return f[n]

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(n):
            if (s[i] == '0'):
                f[i + 1] = f[i - 1] if i and s[i - 1] in ['1', '2'] else 0
            else:
                f[i + 1] = f[i]
                if (i and (s[i - 1] == '1' or (s[i - 1] == '2' and ord(s[i]) <= ord('6')))):
                    f[i + 1] += f[i - 1]
        return f[n]
