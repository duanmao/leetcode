class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbrs = {}
        for word in dictionary:
            abbr = self.__getAbbr(word)
            if (abbr in self.abbrs and self.abbrs[abbr] != word):
                self.abbrs[abbr] = "" # already impossible to be unique
            else:
                self.abbrs[abbr] = word

    def isUnique(self, word: str) -> bool:
        abbr = self.__getAbbr(word)
        return abbr not in self.abbrs or self.abbrs[abbr] == word

    def __getAbbr(self, word):
        if (len(word) < 3):
            abbr = word
        else:
            abbr = word[0] + str(len(word) - 2) + word[-1]
        return abbr


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbrs = collections.defaultdict(set)
        for word in dictionary:
            self.abbrs[self.__getAbbr(word)].add(word)

    def isUnique(self, word: str) -> bool:
        abbr = self.__getAbbr(word)
        if (abbr not in self.abbrs): return True
        return word in self.abbrs[abbr] and len(self.abbrs[abbr]) == 1
        
    def __getAbbr(self, word):
        if (len(word) < 3):
            abbr = word
        else:
            abbr = word[0] + str(len(word) - 2) + word[-1]
        return abbr


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
