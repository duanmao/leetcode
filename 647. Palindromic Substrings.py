# Time: O(n^2), space: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindromic(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        count = 0
        for i in range(len(s)):
            count += palindromic(i, i)
            count += palindromic(i, i + 1)
        return count

# O(n) algorithm: Manacher's algorithm
# https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/
# too complicated for me to understand though...
