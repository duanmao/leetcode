# https://leetcode.com/problems/reorganize-string/solution/

# Time: O(n), space: O(n) (most_common(k) uses heap that complexity is O(nlogk)) 
# no need to sort, just find the most common chars and save it to the last
from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        if (not S): return ""
        n = len(S)
        counts = Counter(S)
        maxc, maxcount = counts.most_common(1)[0]
        if (maxcount > (n + 1) / 2): return ""
        del counts[maxc]
        chars = []
        for c in counts:
            chars.extend(counts[c] * [c])
        chars.extend(maxcount * [maxc])
        res = [None] * n
        res[::2], res[1::2] = chars[n//2:], chars[:n//2]
        return "".join(res)

# Time: O(NlogA) where A is the size of alphabet, thus it's essentially O(N) since alphabet is
# limited; Space: O(N)
class Solution:
    def reorganizeString(self, S: str) -> str:
        n = len(S)
        sortedChars = [] # chars sorted by their occurences, the more the later
        for c, x in sorted((S.count(x), x) for x in set(S)):
            if (c > (n + 1) / 2): return ""
            sortedChars.extend(c * x)
        ans = [None] * n
        # even slots, odd slots = later half (possibly more chars), earlier half
        ans[::2], ans[1::2] = sortedChars[n//2:], sortedChars[:n//2]
        return "".join(ans)

# use heap
from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        counts = Counter(S)
        pq = [(-counts[c], c) for c in counts]
        heapq.heapify(pq)
        if (-pq[0][0] > (len(S) + 1) / 2):
            return ""

        ans = []
        while len(pq) >= 2:
            # We pop the top two elements from the heap (representing different letters with positive remaining count), 
            # and then write the most frequent one that isn't the same as the most recent one written.
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            
            #This code turns out to be superfluous, but explains what is happening
            #if not ans or ch1 != ans[-1]:
            #    ans.extend([ch1, ch2])
            #else:
            #    ans.extend([ch2, ch1])
            ans.extend([ch1, ch2])
            
            # push the correct counts back onto the heap.
            if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

        return "".join(ans) + (pq[0][1] if pq else '')
