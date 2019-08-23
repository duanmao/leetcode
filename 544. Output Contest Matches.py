# O(n) IMO, but.. others say it's O(nlogn)

class Solution:
    def findContestMatch(self, n: int) -> str:
        matches = list(range(1, n + 1))
        left, right = 0, len(matches) - 1
        while (right > 0):
            left = 0
            while (left < right):
                matches[left] = (matches[left], matches[right])
                left += 1
                right -= 1
            right = left - 1
        return str(matches[0]).replace(' ', '')

class Solution:
    def findContestMatch(self, n: int) -> str:
        matches = list(range(1, n + 1))
        while (len(matches) > 1):
            compete = []
            left, right = 0, len(matches) - 1
            while (left < right):
                compete.append((matches[left], matches[right]))
                left += 1
                right -= 1
            matches = compete
        return str(matches[0]).replace(' ', '')
