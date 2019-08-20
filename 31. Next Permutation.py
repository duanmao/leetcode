# O(n)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i,  j = n - 2, n - 1
        while (i >= 0 and nums[i] >= nums[i + 1]): i -= 1
        if (i >= 0):
            while (j > i and nums[j] <= nums[i]): j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j = n - 1
        while (i < j):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (len(nums) < 2): return
        n = len(nums)
        for i in range(n - 1)[::-1]:
            if (nums[i] < nums[i + 1]): break
        for j in range(n)[::-1]:
            if (nums[j] > nums[i]): break
        nums[i], nums[j] = nums[j], nums[i]
        if (i != j): i += 1
        j = n - 1
        while (i < j):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
