class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def restore(idx, cuts):
            if idx == len(s):
                # don't forget to check the number of cuts
                if len(cuts) == 4: res.append(".".join(cuts))
                return
            if len(cuts) >= 4: return
            restore(idx + 1, cuts + [s[idx]])
            if s[idx] == '0': return
            for l in range(2, 4):
                if idx + l <= len(s): # don't forget to check the index boundary
                    num = int(s[idx:idx + l])
                    if num <= 255:
                        restore(idx + l, cuts + [s[idx:idx + l]])

        restore(0, [])
        return res
