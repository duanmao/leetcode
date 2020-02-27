# bidirectional BFS
# Time: O(MN), space: O(MN), same as the regular BFS, but emprically much faster
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dic = set(wordList)
        if endWord not in dic: return 0
        dic.discard(beginWord)
        dic.remove(endWord)
        qBegin, qEnd = collections.deque([beginWord]), collections.deque([endWord])
        vstBegin, vstEnd = {beginWord: 1}, {endWord: 1}

        def transform(word, queue, visited, otherVisited):
            for i in range(len(word)):
                w = list(word)
                for c in string.ascii_lowercase:
                    w[i] = c
                    nword = "".join(w)
                    if nword in otherVisited:
                        return visited[word] + otherVisited[nword]
                    if nword in dic:
                        queue.append(nword)
                        visited[nword] = visited[word] + 1
                        dic.remove(nword)
            return None

        while qBegin and qEnd:
            bWord = qBegin.popleft()
            eWord = qEnd.popleft()
            forward = transform(bWord, qBegin, vstBegin, vstEnd)
            if forward: return forward
            backward = transform(eWord, qEnd, vstEnd, vstBegin)
            if backward: return backward
        return 0

# BFS
# Time: O(M*N), where N is size of the dictionary and M is length of the word.
# Space: O(M*N)
# possible improvement: bidirectional BFS, check for prefix matching
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dic = set(wordList)
        if endWord not in dic: return 0
        letters = string.ascii_lowercase
        dic.discard(beginWord)
        queue = collections.deque([(beginWord, 1)])
        while queue:
            word, step = queue.popleft()
            for i in range(len(word)):
                w = list(word)
                for c in letters:
                    w[i] = c
                    nword = "".join(w)
                    if nword in dic:
                        if nword == endWord: return step + 1
                        queue.append((nword, step + 1))
                        dic.remove(nword)
        return 0
