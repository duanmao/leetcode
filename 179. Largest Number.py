# Time: O(nklogn) where n is the array length and k is the average length of the nums
# Since compare 2 strings will take O(k), sorting will take O(nlogn)
# Each level does O(kn) comparisons and there are O(logn) levels (consider mergesort)
# Space: O(n)
import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = [ str(num) for num in nums ]
        strs.sort(key = functools.cmp_to_key(lambda x, y: 1 if x + y < y + x else 0 if x + y == y + x else -1))
        return "".join(strs).lstrip("0") or "0"
