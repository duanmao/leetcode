# O(1) solution exists: https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm
# https://www.cnblogs.com/nullzx/p/7499397.html
# but too complicated to finish in an interview for me... so... 


class StreamChecker:

    def __init__(self, words: List[str]):
        self.tails = collections.defaultdict(set)
        for word in words:
            self.tails[word[-1]].add(word)
        self.input = ""

    def query(self, letter: str) -> bool:
        self.input += letter
        return any(self.input.endswith(word) for word in self.tails[letter])


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

# AC but slow than the previous one, which is... weird
# the words should be entered into the Trie reversely
class TrieNode:
    def __init__(self, c, isEnd = False):
        self.val = c
        self.children = {}
        self.isEnd = isEnd

class StreamChecker:

    def __init__(self, words: List[str]):
        self.tails = collections.defaultdict(set)
        self.root = TrieNode(' ')

        def buildTrie(word):
            node = self.root
            for c in word:
                if (c not in node.children):
                    node.children[c] = TrieNode(c)
                node = node.children[c]
            node.isEnd = True

        for word in words:
            buildTrie(word[::-1])
        self.input = ""

    def query(self, letter: str) -> bool:
        self.input += letter
        node = self.root
        for c in self.input[::-1]:
            if (c in node.children):
                node = node.children[c]
                if (node.isEnd): return True
            else:
                return False
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
