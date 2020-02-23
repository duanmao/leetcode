# Time: O(n), space: O(1)
class Solution:
    def compress(self, chars: List[str]) -> int:
        w = r = 0 # write and read pointer
        while r < len(chars):
            chars[w] = chars[r]
            count = 0
            while r < len(chars) and chars[r] == chars[w]:
                r += 1
                count += 1
            w += 1
            if count > 1:
                cts = str(count)
                chars[w:w+len(cts)] = cts
                w += len(cts)
        return w
