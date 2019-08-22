# O(n)? O(n^2) at most, cannot be sure of the lower bound though
# a cleaner version:
# https://leetcode.com/problems/parse-lisp-expression/discuss/113902/A-Clean-Java-Solution/212705
# a stack version, though I don't quite comprehend..
# https://leetcode.com/problems/parse-lisp-expression/discuss/109709/python-solution-using-stacks.
class Solution:
    def evaluate(self, expression: str) -> int:
        def evl(exp, varis):
            if (exp.replace('-', '').isnumeric()): return int(exp)
            if (exp.find(' ') == -1): return varis[exp]
            
            # split the expression into operable parts so that we can
            # deal with them sequentially later
            level = 0
            splitted = []
            cur = ""
            for i, c in enumerate(exp):
                if (c == '('):
                    if (level == 1):
                        start = i
                    level += 1
                elif (level == 1):
                    if (c == ' ' or c == ')'): # don't forget the last one when c == ')', essentially i == len(exp) - 1
                        if (cur): # important check too
                            splitted.append(cur)
                            cur = ""
                    else:
                        cur += c
                elif (c == ')'):
                    level -= 1
                    if (level == 1):
                        splitted.append(exp[start:i + 1])
            
            e = splitted[0] # valid expression must begin with an operator
            if (e in ['mult', 'add']):
                num1, num2 = splitted[1], splitted[2]
                if (e == 'add'):
                    return evl(num1, varis) + evl(num2, varis)
                else: 
                    return evl(num1, varis) * evl(num2, varis)
            else: # 'let'
                innervaris = varis.copy() # handle variable value scope
                i = 1
                while (i < len(splitted)):
                    if (i + 1 < len(splitted)):
                        var, val = splitted[i], splitted[i + 1]
                        i += 2
                        innervaris[var] = evl(val, innervaris)
                    else:
                        return evl(splitted[i], innervaris)
            return 0
        
        return evl(expression, {})
