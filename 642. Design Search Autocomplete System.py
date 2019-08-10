class TrieNode:
    def __init__(self, c):
        self.val = c
        self.children = {}
        self.times = 0
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.current = ""
        self.root = TrieNode("")
        for i, sentence in enumerate(sentences):
            self.__add(sentence, times[i])

    def input(self, c: str) -> List[str]:
        if (c == '#'):
            self.__add(self.current, 1)
            self.current = ""
            return []
        self.current += c
        sentences = self.__search(self.current)
        top3 = sorted(sentences)[:3]
        return [s[1] for s in top3]

    def __add(self, sentence, times):
        node = self.root
        for c in sentence:
            if (c not in node.children): node.children[c] = TrieNode(c)
            node = node.children[c]
        node.times += times
        
    def __search(self, prefix):
        node = self.root
        for c in prefix:
            if (c in node.children): node = node.children[c]
            else: return []
        res = []
        self.__dfs(prefix, node, res)
        return res
    
    def __dfs(self, prefix, node, res):
        if (node.times):
            res.append((-node.times, prefix)) # we want times sorted in descending order
        for c in node.children:
            self.__dfs(prefix + c, node.children[c], res)

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
