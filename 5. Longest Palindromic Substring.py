# Time: O(n^2), space: O(1)
# the upper one below is supposed to take slightly less time, but essentially they're the same
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while (left >= 0 and right < len(s)):
                if (s[left] == s[right]):
                    left -= 1
                    right += 1
                else: break
            return left + 1, right

        l = r = 0
        for i in range(len(s)):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i + 1)
            if (r1 - l1 > r - l):
                l = l1
                r = r1
            if (r2 - l2 > r - l):
                l = l2
                r = r2
        return s[l:r]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while (left >= 0 and right < len(s)):
                if (s[left] == s[right]):
                    left -= 1
                    right += 1
                else: break
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            s1 = expand(i, i)
            s2 = expand(i, i + 1)
            if (len(longest) < len(s1)):
                longest = s1
            if (len(longest) < len(s2)):
                longest = s2
        return longest
