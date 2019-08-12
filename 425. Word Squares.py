# https://leetcode.com/problems/word-squares/discuss/91333/Explained.-My-Java-solution-using-Trie-126ms-1616
# Time: worst O(n*l^2 + n*n^l), n: # of words, l: length of a word
# https://zhuhan0.blogspot.com/2017/09/leetcode-425-word-squares.html
# don't understand the exponential part as always...
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words)
        prefixes = collections.defaultdict(list)
        for w in words:
            for i in range(len(w)):
                prefixes[w[:i + 1]].append(w)
                
        res = []
        
        def check(cur):
            if (len(cur) == len(cur[0])):
                res.append(cur[:])
            else:
                idx = len(cur)
                pref = ""
                for i in range(idx):
                    pref += cur[i][idx]
                for w in prefixes[pref]:
                    cur.append(w)
                    check(cur)
                    cur.pop()
        
        for w in words:
            check([w])
        return res
