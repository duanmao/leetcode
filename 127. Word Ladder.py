# BFS
# Time: O(N*M*M), where N is size of the dictionary and M is length of the word.
# Space: O(N)
# possible improvement: bidirectional BFS, check for prefix matching
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList):
            return 0
        wordList = set(wordList)
        words = deque([(beginWord, 1)])
        while (len(words)):
            curword, step = words.popleft()
            for i in range(len(curword)):
                prefix = curword[:i]
                for c in string.ascii_lowercase:
                    nextword = curword[:i] + c + curword[i+1:]
                    if (nextword == endWord):
                        return step + 1
                    if (nextword in wordList):
                        words.append((nextword, step + 1))
                        wordList.remove(nextword)
        return 0
