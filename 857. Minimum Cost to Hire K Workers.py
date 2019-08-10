# Time: O(nlogn), space: O(K)
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/141768/Detailed-explanation-O(NlogN)
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = sorted([(w/q, q) for q, w in zip(quality, wage)])
        mincost = float('inf')
        qualitySum = 0
        heap = []
        for ratio, quality in workers:
            if (len(heap) == K): qualitySum += heapq.heappop(heap)
            heapq.heappush(heap, -quality)
            qualitySum += quality
            if (len(heap) == K):
                mincost = min(mincost, qualitySum * ratio)
        return mincost
