class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if (denominator == 0): return ""
        if (numerator == 0): return "0"
        neg = False
        if ((numerator < 0) ^ (denominator < 0)):
            neg = True
        numerator, denominator = abs(numerator), abs(denominator)
        res = str(numerator // denominator)
        if (not numerator % denominator): return "-" + res if neg else res
        res += "."
        remains = {}
        while (numerator % denominator):
            rm = numerator % denominator
            if (rm in remains):
                recur = remains[rm]
                res = res[:recur] + "(" + res[recur:] + ")"
                break
            else:
                remains[rm] = len(res)
                numerator = rm * 10
                res += str(numerator // denominator)
        return "-" + res if neg else res
