# Time: O(k*(k^n))? not sure , space: O(k^n)
# de brujin sequence
# https://leetcode.com/problems/cracking-the-safe/discuss/153039/DFS-with-Explanations
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        total = k ** n 
        s = '0' * n
        pwds = {s}
        
        def generate(s):
            if (len(pwds) == total):
                assert(len(s), k ** n + n - 1)
                return s
            for i in range(k):
                s1 = s + str(i)
                cur = s1[-n:]
                if (cur not in pwds):
                    pwds.add(cur)
                    pwd = generate(s1)
                    if (pwd):
                        return pwd
                    pwds.remove(cur)
            return ""
        
        return generate(s)

# Time complexity can be O(k^n), see
# https://leetcode.com/problems/cracking-the-safe/solution/ approach #2
