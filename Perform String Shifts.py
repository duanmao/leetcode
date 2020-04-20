class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        lshifts = 0
        for drc, amount in shift:
            if drc: lshifts -= amount
            else: lshifts += amount
        lshifts %= len(s)
        return s[lshifts:] + s[:lshifts]
