# Time: O(n), space: O(n)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        for intv in intervals:
            if (intv[1] < newInterval[0]):
                left.append(intv)
            elif (intv[0] > newInterval[1]):
                right.append(intv)
            else:
                newInterval[0] = min(newInterval[0], intv[0])
                newInterval[1] = max(newInterval[1], intv[1])
        return left + [newInterval] + right

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge(res, interval):
            if (res and res[-1][1] >= interval[0]):
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
            
        n = len(intervals)
        res = []
        i = 0
        for i in range(n):
            if (intervals[i][0] < newInterval[0]):
                res.append(intervals[i])
            else:
                break
        merge(res, newInterval)
        for j in range(i, n):
            merge(res, intervals[j])
        return res
