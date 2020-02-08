# Time: O(n), space: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        
        def expand(num, step):
            l = 0
            while num in numset:
                numset.remove(num)
                num += step
                l += 1
            return l
        
        maxlen = 0
        while numset:
            num = next(iter(numset))
            maxlen = max(maxlen, expand(num, -1) + expand(num + 1, 1))
        return maxlen
