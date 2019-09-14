# https://leetcode.com/problems/string-transforms-into-another-string/discuss/355382/JavaC%2B%2BPython-Need-One-Unused-Character
# https://leetcode.com/problems/string-transforms-into-another-string/discuss/355412/Python-simple-O(n)-with-explanation
# Time: O(n), space: O(1)
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if (str1 == str2): return True
        if (len(str1) != len(str2)): return False
        mapping = {}
        for i, c in enumerate(str1):
            if mapping.get(c) and mapping[c] != str2[i]:
                return False
            mapping[c] = str2[i]
        return len(set(str2)) < 26 # same as len(set(mapping.values())) < 26
