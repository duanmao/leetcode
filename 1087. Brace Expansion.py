class Solution:
    def expand(self, S: str) -> List[str]:
        if (S.find('{') == -1): return [S]
        res = []
        for i, c in enumerate(S):
            if (c == "{"):
                j = S.find("}", i)
                left = self.expand(S[:i])
                right = self.expand(S[j + 1:])
                for l in left:
                    for r in right:
                        for c in S[i+1:j].split(','):
                            res.append(l + c + r)
                return sorted(res)
        return res

class Solution:
    def expand(self, S: str) -> List[str]:
        groups = S.replace('}', '{').split('{')
        groups = [group.split(',') for group in groups]
        return sorted(map("".join, itertools.product(*groups)))

class Solution:
    def expand(self, S: str) -> List[str]:
        groups = []
        group = []
        cur = ""
        for i, c in enumerate(S):
            if c not in {'{', '}', ','}:
                cur += c 
            if c in {'{', '}', ','} or i == len(S) - 1:
                if cur: group.append(cur)
                cur = ""
                if c in {'{', '}'} or i == len(S) - 1:
                    if group:
                        groups.append(group)
                    group = []
        return sorted(map("".join, itertools.product(*groups)))
