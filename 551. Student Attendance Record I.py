class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        for i, c in enumerate(s):
            if (c == 'A'):
                absent += 1
                if (absent > 1): return False
            elif (c == 'L'):
                if (i >= 2 and s[i - 1] == s[i - 2] == 'L'):
                    return False
        return True
