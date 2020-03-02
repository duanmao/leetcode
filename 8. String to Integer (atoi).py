class Solution:
    def myAtoi(self, str: str) -> int:
        def parse(s):
            num = 0
            for c in s:
                if c.isdigit(): num = num * 10 + int(c)
                else: break
            return num

        str = str.strip()
        if not str: return 0
        if not str[0].isdigit() and str[0] not in {'-', '+'}: return 0
        if str[0].isdigit():
            return min(2**31 - 1, parse(str))
        else:
            num = parse(str[1:])
            if str[0] == '-':
                return max(-2**31, -num)
            else:
                return min(2**31 - 1, num)

class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if (not str): return 0
        neg = False
        if (not str[0].isdigit()):
            if (str[0] == '-' or str[0] == '+'):
                neg = str[0] == '-'
            else:
                return 0
        res = 0
        start = 0 if str[0].isdigit() else 1
        for i in range(start, len(str)):
            if (str[i].isdigit()):
                res = res * 10 + int(str[i])
            else:
                break
        res = res if not neg else -res
        # stupid stuff just to pass the OJ
        # res = res if res <= 2147483647 else 2147483647
        # res = res if res >= -2147483648 else -2147483648
        return res
