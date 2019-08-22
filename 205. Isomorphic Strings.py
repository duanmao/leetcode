# Time: O(n), space: O(2*1)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        dicts, dictt = {}, {}
        for i in range(len(s)):
            if (dicts.get(s[i]) != dictt.get(t[i])):
                return False
            dicts[s[i]] = i
            dictt[t[i]] = i
        return True

# fastest empirically, though not theoretically
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

# Time: O(n), space: O(2*1)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        dicts, dictt = {}, {}
        for i in range(len(s)):
            if (s[i] not in dicts): dicts[s[i]] = t[i]
            if (t[i] not in dictt): dictt[t[i]] = s[i]
            if (dicts.get(s[i]) != t[i] or dictt.get(t[i]) != s[i]):
                return False
        return True

# Time: O(2n), space: O(1)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        
        def check(s, t):
            dic = {}
            for i in range(len(s)):
                if (s[i] not in dic):
                    dic[s[i]] = t[i]
                if (dic[s[i]] != t[i]):
                    return False
            return True
    
        return check(s, t) and check(t, s)
