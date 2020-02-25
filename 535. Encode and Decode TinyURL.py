# https://leetcode.com/problems/encode-and-decode-tinyurl/discuss/100268/Two-solutions-and-thoughts
# Analysis:
# * with len = 6, at most (10+26*2)6 = 56,800,235,584 codes (unique urls) can be accommodated
# * random entries prevents the generated short urls from being predicted
# * duplicate long urls won't have different entries, so that no memory will be wasted
# * possible collisions, and the number of collisions could increase with the increasing number of
# input strings, leading to performance degradation. (same as generating hash codes)
class Codec:

    alphabet = string.ascii_letters + string.digits

    def __init__(self):
        self.long2key = {}
        self.key2long = {}
        self.len = 6

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.long2key:
            key = ''.join(random.choices(Codec.alphabet, k = self.len))
            if key not in self.key2long:
                self.key2long[key] = longUrl
                self.long2key[longUrl] = key
        return 'http://tinyurl.com/' + self.long2key[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.key2long[shortUrl[-self.len:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
