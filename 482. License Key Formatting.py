class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.upper().replace('-', '')
        n = len(S)
        groups = [S[i-K+1:i+1] for i in range(n)[::-K]]
        if (groups and not groups[-1]): groups[-1] = S[:n - n // K * K]
        return "-".join(groups[::-1])
