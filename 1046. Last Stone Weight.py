from heapq import *

# Time: O(nlogn), space: O(n)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-st for st in stones]
        heapify(maxHeap)
        while len(maxHeap) > 1:
            hv1 = heappop(maxHeap)
            hv2 = heappop(maxHeap)
            if hv1 != hv2:
                heappush(maxHeap, -abs(hv1 - hv2))
        return -maxHeap[0] if maxHeap else 0
