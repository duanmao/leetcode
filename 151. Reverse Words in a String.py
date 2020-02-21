# Time: O(n), space: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        words = [w[::-1] for w in s.split()]
        rs = " ".join(words)[::-1]
        return rs
