# Time: O(n), space: O(1)
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def addrange(start, end, res):
            if (start == end): res.append(str(start))
            else: res.append("->".join([str(start), str(end)]))
                
        start = lower
        res = []
        for i in nums:
            if (i < lower):
                start = lower
            else:
                if (i > start):
                    addrange(start, i - 1, res)
                start = i + 1
        if (start <= upper):
            addrange(start, upper, res)
        return res
