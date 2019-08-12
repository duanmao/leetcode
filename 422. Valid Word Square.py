class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        for i in range(n):
            for j in range(len(words[i])):
                if (j >= n or len(words[j]) <= i or words[i][j] != words[j][i]):
                    return False
        return True
