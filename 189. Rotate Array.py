# Time: O(n), space: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i1, i2):
            nums[i1], nums[i2] = nums[i2], nums[i1]

        start = 0
        n = len(nums)
        while (start < n and k):
            k %= (n - start) # # of numbers left to rotate
            for i in range(k):
                swap(start + i, n - k + i)
            start += k

# Time: O(n), space: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate(nums, low, high, k):
            def swap(i1, i2):
                nums[i1], nums[i2] = nums[i2], nums[i1]

            k %= (high - low)
            if (k == 0):
                return
            for i in range(k):
                swap(low + i, high - k + i)
            rotate(nums, low + k, high, k)

        rotate(nums, 0, len(nums), k)

# Time: O(n), space: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, low, high):
            while (low < high):
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1
        
        n = len(nums)
        k %= n
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
