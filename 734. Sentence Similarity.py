class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        pairs = set(map(tuple, pairs))
        if (len(words1) != len(words2)): return False
        for w1, w2 in zip(words1, words2):
            if (w1 != w2 and (w1, w2) not in pairs and (w2, w1) not in pairs):
                return False
        return True
