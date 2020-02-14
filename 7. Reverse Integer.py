class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)
        newx = 0
        while x:
            # print(newx, x)
            newx *= 10
            newx += x % 10
            x = int(x / 10)
        if negative:
            return -newx if -newx > -2 ** 31 else 0
        else:
            return newx if newx < 2 ** 31 - 1 else 0
