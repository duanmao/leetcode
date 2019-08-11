class Solution:
    def decodeString(self, s: str) -> str:
        stack = [["", 1]]
        cur = ""
        for c in s:
            if (c.isdigit()):
                cur += c
            elif (c == '['):
                stack.append(["", int(cur)])
                cur = ""
            elif (c == ']'):
                s, times = stack.pop()
                stack[-1][0] += s * times
            else:
                stack[-1][0] += c
        return stack[0][0]
