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
        A = S.replace('}', '{').split('{')
        # print(A)
        B = [sorted(a.split(',')) for a in A]
        # print(B)
        # print(list(itertools.product(*B)))
        return [''.join(c) for c in itertools.product(*B)]
