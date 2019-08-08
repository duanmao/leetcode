# O(k^(k^n))? not sure
# de brujin sequence
# https://leetcode.com/problems/cracking-the-safe/discuss/153039/DFS-with-Explanations
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        total = pow(k, n)
        s = '0' * n
        pwds = {s}
        
        def generate(s, pwds, total):
            if (len(pwds) == total): return s
            for i in range(k):
                s1 = s + str(i)
                cur = s1[-n:]
                if (cur not in pwds):
                    pwds.add(cur)
                    pwd = generate(s1, pwds, total)
                    if (pwd):
                        return pwd
                    pwds.remove(cur)
            return ""
        
        return generate(s, pwds, total)
