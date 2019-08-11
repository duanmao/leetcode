# DP


# Divide and Conquer
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        oprs = {"+": operator.add, "-": operator.sub, "*": operator.mul }

        def compute(x, y, opr):
            return oprs[opr](x, y)

        if (input.isdigit()):
            return [int(input)]
        res = []
        for i, c in enumerate(input):
            if (c in "+-*"):
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for l in left:
                    for r in right:
                        res.append(compute(l, r, c))
                        # res.append(eval(str(l) + c + str(r))) # valid but slower
        return res

# add memo
class Solution:
    # memo cannot be simply added inside this function, it's useless in this way
    # instead, we should add it outside or in the function signature
    def diffWaysToCompute(self, input: str, memo = {}) -> List[int]:
        oprs = {"+": operator.add, "-": operator.sub, "*": operator.mul }

        def compute(x, y, opr):
            return oprs[opr](x, y)

        if (input.isdigit()):
            return [int(input)]
        if (input in memo):
            return memo[input]
        res = []
        for i, c in enumerate(input):
            if (c in "+-*"):
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for l in left:
                    for r in right:
                        res.append(compute(l, r, c))
        memo[input] = res
        return res
