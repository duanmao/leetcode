# https://leetcode.com/problems/random-pick-with-blacklist/discuss/146533/Super-Simple-Python-AC-w-Remapping
# https://leetcode.com/problems/random-pick-with-blacklist/solution/ - Virtual whitelist
# Time: init: O(B), pick: O(1)
# Space: O(B) at most
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.total = N - len(blacklist)
        blacklist = set(blacklist)
        self.replace = {}
        white = self.total
        for b in blacklist:
            if (b < self.total):
                while (white in blacklist): white += 1
                self.replace[b] = white
                white += 1

    def pick(self) -> int:
        i = random.randint(0, self.total - 1)
        return self.replace.get(i) or i

# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()


# Binary search
# https://leetcode.com/problems/random-pick-with-blacklist/discuss/146545/Simple-Java-solution-with-Binary-Search
# though I just cannot understand it clearly... AHHHH my brain is exploding
