class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        oprs = {"+", "-", "*", "/"}
        for tk in tokens:
            if (tk in oprs):
                opr2 = operands.pop()
                opr1 = operands.pop()
                if (tk == "+"):
                    operands.append(opr1 + opr2)
                elif (tk == "-"):
                    operands.append(opr1 - opr2)
                elif (tk == "*"):
                    operands.append(opr1 * opr2)
                else:
                    operands.append(int(opr1 / opr2))
            else:
                operands.append(int(tk))
        return operands.pop()
