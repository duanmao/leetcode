class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (not strs):
            return ""
        pref = strs[0]
        for i in range(1, len(strs)):
            pref = pref[:min(len(pref), len(strs[i]))] # important
            for j in range(len(pref)):
                if (not pref[j] == strs[i][j]):
                    pref = pref[:j]
                    break
        return pref
