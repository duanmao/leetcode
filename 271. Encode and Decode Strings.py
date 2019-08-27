# Time: O(n), space: O(n)
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        def lengthPrefix(s):
            return "%d:" % len(s)

        return "".join(lengthPrefix(s) + s for s in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        decoded = []
        i = 0
        while (i < len(s)):
            j = s.find(':', i)
            l = int(s[i:j])
            i = j + l + 1
            decoded.append(s[j + 1:i])
        return decoded

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
