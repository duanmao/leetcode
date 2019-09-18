# Time: O(nlogn), space: O(n)
from heapq import *
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counts = collections.Counter(hand)
        minheap = [[val, ct] for val, ct in counts.items()]
        heapify(minheap)
        while (minheap):
            val, count = heappop(minheap)
            left = []
            for i in range(1, W):
                if minheap:
                    nxt, ncount = heappop(minheap)
                    if (nxt == val + i and ncount >= count):
                        if (ncount > count): left.append([nxt, ncount - count])
                    else:
                        return False
                else:
                    return False
            for lf in left:
                heappush(minheap, lf)
        return True

# https://leetcode.com/problems/hand-of-straights/discuss/135598/C%2B%2BJavaPython-O(MlogM)-Complexity
# Time: O(nlogn), space: O(n)
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counts = collections.Counter(hand)
        starts = collections.deque()
        lastval, opened = -1, 0
        for val in sorted(counts):
            if counts[val] < opened or (opened and val != lastval + 1):
                return False
            starts.append(counts[val] - opened)
            opened = counts[val]
            lastval = val
            if len(starts) == W: opened -= starts.popleft()
        return opened == 0

# straightforward
# Time: O(n/w * n), space: O(n)
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counts = collections.Counter(hand)
        while counts:
            start = min(counts)
            need = counts[start]
            for i in range(start, start + W):
                if (i in counts and counts[i] >= need):
                    counts[i] -= need
                    if (counts[i] == 0):
                        del counts[i]
                else:
                    return False
        return True

# slightly slower than the above one but even more starightforward
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counts = collections.Counter(hand)
        while counts: # O(n/w)
            start = min(counts) # O(n)
            for i in range(start, start + W):
                if (counts.get(i)):
                    counts[i] -= 1
                    if (counts[i] == 0):
                        del counts[i]
                else:
                    return False
        return True
