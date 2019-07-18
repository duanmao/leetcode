# Time: O(nlogn), space: O(1)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def sortFirst(val):
            return val[0]
        intervals.sort(key = sortFirst)
        merged = []
        for intv in intervals:
            if (len(merged) and intv[0] <= merged[-1][1]):
                merged[-1][1] = max(intv[1], merged[-1][1]) # check merged[-1][1]
            else:
                merged.append(intv)
        return merged
