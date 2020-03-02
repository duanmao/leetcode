# Time: O(n), space: O(n)
class Solution:
    def calculate(self, s: str) -> int:
        def cal(s, i):
            stack = []
            num = 0
            opr = '+'
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] == '(':
                    num, i = cal(s, i + 1)
                else:
                    if opr == '*':
                        stack.append(stack.pop() * num)
                    elif opr == '/':
                        stack.append(int(stack.pop() / num)) # must use int(), cannot use //
                    else:
                        stack.append(-num if opr == '-' else num)
                    if s[i] == ')': # must evaluate previous result before checking ')' 
                        return sum(stack), i
                    opr = s[i]
                    num = 0
                i += 1
            return sum(stack), i
        
        s = s.replace(' ', '') + '$'
        res, _ = cal(s, 0)
        return res
