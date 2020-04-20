# Time: O(n), space: O(1)
# https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pos = {0: -1}
        count = maxLen = 0
        for i, num in enumerate(nums):
            if num == 0: count -= 1
            else: count += 1
            # if the current count has already appeared before,
            # it means from the last position it shows up until now,
            # the counts of 0s and 1s are equal
            if count in pos: maxLen = max(maxLen, i - pos[count])
            else: pos[count] = i
        return maxLen
