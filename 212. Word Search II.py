class TrieNode:
    def __init__(self, c = None):
        self.c = c
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if (c not in node.children):
                node.children[c] = TrieNode(c)
            node = node.children[c]
        
    def startWith(self, prefix):
        node = self.root
        for c in prefix:
            if (c not in node.children):
                return False
            node = node.children[c]
        return True
    
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        hor = [0, 0, -1, 1]
        ver = [-1, 1, 0, 0]
        if (not board or not board[0]):
            return []
        foundwords = set()
        words = set(words)
        trie = Trie()
        for word in words:
            trie.insert(word)
        m = len(board)
        n = len(board[0])    
        visited = [[False] * n for i in range(m)]
        
        def dfs(row, col, cur):
            # print(cur)
            if (row < 0 or row >= m or col < 0 or col >= n or visited[row][col]):
                return
            cur += board[row][col]
            if (not trie.startWith(cur)):
                return
            if (cur in words):
                foundwords.add(cur)
            visited[row][col] = True
            for k in range(4):
                dfs(row + hor[k], col + ver[k], cur)
            visited[row][col] = False
            
        for i in range(m):
            for j in range(n):
                dfs(i, j, "")
        return foundwords
