class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-", "").upper()[::-1]
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '').upper()
        segments = [S[max(0, i-K):i] for i in range(len(S), 0, -K)]
        return "-".join(segments[::-1])

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.upper().replace('-', '')
        n = len(S)
        groups = [S[i-K+1:i+1] for i in range(n)[::-K]]
        if (groups and not groups[-1]): groups[-1] = S[:n - n // K * K]
        return "-".join(groups[::-1])
