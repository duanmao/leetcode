class Solution:
    def calculate(self, s: str) -> int:
        opr = '+'
        res = 0
        stack = []
        s = s.replace(' ', '')
        num = 0
        for i, c in enumerate(s):
            if (c.isdigit()):
                num = (num * 10 + ord(c) - ord('0'))
            if (not c.isdigit() or i == len(s) - 1):
                if (opr == '*'):
                    stack.append(stack.pop() * num)
                elif (opr == '/'):
                    stack.append(int(stack.pop() / num))
                else:
                    stack.append(-num if opr == '-' else num)
                opr = c
                num = 0
        return sum(stack)

class Solution:
    def calculate(self, s: str) -> int:
        def getNum(s, start):
            numstr = ""
            while (start < len(s) and s[start].isdigit()):
                numstr += s[start]
                start += 1
            print(numstr)   
            return int(numstr), start
            
        s = s.replace(' ', '')
        res = 0
        ptr = 0
        while (ptr < len(s)):
            if (s[ptr].isdigit()):
                num, ptr = getNum(s, ptr)
            elif (s[ptr] == '*' or s[ptr] == '/'):
                mul = s[ptr] == '*'
                num2, ptr = getNum(s, ptr + 1)
                num = num * num2 if mul else int(num / num2)
            else:
                res += num
                neg = True if s[ptr] == '-' else False
                num, ptr = getNum(s, ptr + 1)
                num *= (-1 if neg else 1)
            print(num, res)
        res += num
        return res
