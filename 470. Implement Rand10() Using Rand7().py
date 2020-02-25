# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            a, b = rand7(), rand7()
            num = (a - 1) * 7 + b
            if num <= 40:
                return (num - 1) % 10 + 1
        return 0
