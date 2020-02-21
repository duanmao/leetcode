# Brute Force
# Time: O(2^n)
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for a in arr:
            if len(set(a)) < len(a): continue
            a = set(a)
            for s in dp:
                if a & s: continue
                dp.append(a | s)
        return max(len(s) for s in dp)

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        self.maxlen = 0
        
        def generate(cur, s):
            if cur == len(arr): return
            for i in range(cur, n):
                if len(set(arr[i])) != len(arr[i]):
                    continue
                if len(set(s + arr[i])) == len(s + arr[i]):
                    self.maxlen = max(self.maxlen, len(s + arr[i]))
                    generate(i + 1, s + arr[i])
                    
        generate(0, "")
        return self.maxlen
