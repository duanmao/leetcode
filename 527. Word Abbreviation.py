# Time: O(nl) where l is the average length of the words
# Space: O(n)
# same as below, but using Trie to check the common prefix for words in a group instead of sorting
# However, empirically on OJ, this version is the slowest among the all, much much slower than the sorting
# version below (10 times slower), the reason for which is beyond my ken; and also takes the most space
class TrieNode:
    def __init__(self, val, count):
        self.val = val
        self.count = count
        self.children = {}
        
class Solution:
    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        def abbreviate(word, i = 1):
            abb = word[:i] + str(len(word) - i - 1) + word[-1]
            if (len(abb) >= len(word)): return word
            return abb
        
        def buildTrie(words):
            root = TrieNode(' ', 0)
            for word in words:
                node = root
                for c in word:
                    if (c not in node.children):
                        node.children[c] = TrieNode(c, 1)
                    else:
                        node.children[c].count += 1
                    node = node.children[c]
            return root
        
        def uniquePrefixLen(root, word):
            node = root
            for i, c in enumerate(word):
                if (node.children[c].count == 1):
                    return i + 1
                node = node.children[c]
            return -1
            
        groups = collections.defaultdict(list)
        for i, word in enumerate(dict):
            groups[word[0], len(word), word[-1]].append((word, i))
            
        abbrs = [""] * len(dict)
        for words_inds in groups.values():
            trie = buildTrie([word for word, _ in words_inds])
            for word, i in words_inds:
                prelen = uniquePrefixLen(trie, word)
                abbrs[i] = abbreviate(word, prelen)
        return abbrs

# Time: O(nl*logn) where l is the average length of the words
# Space: O(n)
# Two words are only eligible to have the same abbreviation if they have the same first letter, last letter, and length. Let's group each word based on these properties, and then sort out the conflicts.
# In each group G, if a word W has a longest common prefix P with any other word X in G, then our abbreviation must contain a prefix of more than |P| characters. The longest common prefixes must occur with words adjacent to W (in lexicographical order), so we can just sort G and look at the adjacent words.
class Solution:
    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        def abbreviate(word, i = 1):
            abb = word[:i] + str(len(word) - i - 1) + word[-1]
            if (len(abb) >= len(word)): return word
            return abb
        
        def commonPrefixLen(w1, w2):
            i = 0
            while (i < min(len(w1), len(w2)) and w1[i] == w2[i]):
                i += 1
            return i
            
        abbrs = [""] * len(dict)
        groups = collections.defaultdict(list)
        for i, word in enumerate(dict):
            groups[word[0], len(word), word[-1]].append((word, i))
        for words_inds in groups.values():
            words_inds.sort()
            prelen = [1] * len(words_inds)
            for i in range(len(words_inds) - 1):
                w1, w2 = words_inds[i][0], words_inds[i + 1][0]
                prelength = commonPrefixLen(w1, w2) + 1
                prelen[i] = max(prelen[i], prelength)
                prelen[i + 1] = max(prelen[i + 1], prelength)
                # must check max above, otherwise, consider case:
                # Input:
                #["like","god","internal","me","internet","interval","intension","face","intrusion","intrution"]
                # Output:
                # ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n","intrut2n"]
                # Expected:
                # ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intrus2n","intrut2n"]
            for i, (word, ind) in enumerate(words_inds):
                abbrs[ind] = abbreviate(word, prelen[i])
        return abbrs

# Time: O(n * l * n * l), l: average length of words
# space: O(n)
class Solution:
    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        def abbreviate(word, i = 1):
            abb = word[:i] + str(len(word) - i - 1) + word[-1]
            if (len(abb) >= len(word)): return word
            return abb
        
        n = len(dict)
        abbrs = [abbreviate(word) for word in dict]
        for i, word in enumerate(dict): # n
            dups = set()
            for j in range(i + 1, n):
                if (abbrs[i] == abbrs[j]): dups.add(j)
            prelen = 1
            while (dups): # l
                prelen += 1
                abbrs[i] = abbreviate(word, prelen)
                for j in list(dups): # n
                    abbrs[j] = abbreviate(dict[j], prelen)
                    if (abbrs[i] != abbrs[j]): dups.remove(j) # l
        return abbrs
