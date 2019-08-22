# http://www.frankmadrid.com/ALudicFallacy/2018/02/28/rotated-digits-leet-code-788/
# Time and space: O(logn)
class Solution:
    def rotatedDigits(self, N: int) -> int:
        same = { 0, 1, 8 }
        valid = { 0, 1, 8, 2, 5, 6, 9 }
        checked_digits = set()
        count = 0
        digits = list(map(int, str(N)))
        # suppose N = 678, we will not check how many good numbers are there
        # in [0, 600), [600, 670), [670, 678)
        # count numbers in each intervals
        for i, d in enumerate(digits):
            validcounts = 7 ** (len(digits) - i - 1)
            samecounts = 3 ** (len(digits) - i - 1)
            # try every number that less than this current digit as replacement
            # in the example above, say now i = 0 so that we're checking in range [0, 600)
            # we will count all good numbers in [0, 100), [100, 200), ..., [500, 600] respectively
            for v in range(d):
                # if this number is valid number, say now v = 1, we are evaluating range [100, 200)
                # we have 2 digits left to choose from the valid numbers, each has 7 valid options
                if (v in valid):
                    count += validcounts
                # if this number is a "same" number, and the previous digits are all "same" number too,
                # then in this range there are not_good numbers which stay the same after rotation,
                # so we need to deduct them from the result
                # as before, we have 2 digits to fill in and each of them have 3 "same number" options
                if (v in same and checked_digits.issubset(same)):
                    count -= samecounts
            # if this current digit is not valid already, say it's 7 in the example above
            # we don't need to continue checking [670, 678) because it cannot be valid
            if (d not in valid):
                return count
            checked_digits.add(d)
        # if all the digits of N are valid, we need check whether it's composed of all same numbers
        return count + (not checked_digits.issubset(same))


# Brute Force
# Time: O(nlogn), space: O(logn)
class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0
        for i in range(1, N + 1):
            s = str(i)
            if (all(d not in '347' for d in s) and
               any(d in '2569' for d in s)):
                count += 1
        return count
