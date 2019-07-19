# Time: O(logn), space: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = end = -1
        n = len(nums)
        low = 0
        high = n - 1
        while (low <= high):
            mid = int((low + high) / 2)
            if (nums[mid] < target):
                low = mid + 1
            else:
                high = mid - 1
        if (0 <= low < n and nums[low] == target): # must check
            start = low
        low = start + 1 
        high = n - 1
        while (low <= high):
            mid = int((low + high) / 2)
            if (nums[mid] <= target):
                low = mid + 1
            else:
                high = mid - 1
        if (0 <= high < n and nums[high] == target): # must check
            end = high
        return [start, end]
