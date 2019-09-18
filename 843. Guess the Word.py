# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

# random a word as the picked one is obviously much faster (O(1)), but with lower hit rate
# use pickLeastMatchWord is much slower (O(n^2)), but it hit the target almost every time
# pickBestWord also nailed it almost every time, and it's a lot faster (O(n))
# for explanation: https://leetcode.com/problems/guess-the-word/discuss/134087/C%2B%2B-elimination-histogram-beats-Minimax
class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def match(s1, s2):
            return sum([s1[i] == s2[i] for i in range(min(len(s1), len(s2)))])
        
        def pickLeastMatchWord(wordlist):
            noMatchCount = dict([(word, 0) for word in wordlist])
            for word in wordlist:
                for other in wordlist:
                    if (match(word, other) == 0):
                        noMatchCount[word] += 1
            return min([(count, word) for word, count in noMatchCount.items()])[1]
        
        def pickBestWord(wordlist):
            if (not wordlist): return "" # just a safety check
            # count occurrances of each letter at each position, which essentially tells us how
            # often each character appears at each position. then we can score every word in
            # the list with this information, in order to find the word that has the most "frequent"
            # constituents overall (gives the max score when summing up each of its char's total
            # occurences at that position), thus it captures the most similarity across all the
            # words in the list, and will eliminate the most of the unmatched words in a query
            count = [[0] * 26 for i in range(len(wordlist[0]))]
            for word in wordlist:
                for i, c in enumerate(word):
                    count[i][ord(c) - ord('a')] += 1
            maxscore, best = 0, ""
            for word in wordlist:
                score = 0
                for i, c in enumerate(word):
                    score += count[i][ord(c) - ord('a')]
                if (score > maxscore):
                    maxscore = score
                    best = word
            return best
            
        for i in range(10):
            # pick = wordlist[random.randint(0, len(wordlist) - 1)]
            # pick = pickLeastMatchWord(wordlist)
            pick = pickBestWord(wordlist)
            matched = master.guess(pick)
            list2 = []
            for word in wordlist:
                if (match(pick, word) == matched):
                    list2.append(word)
            wordlist = list2
