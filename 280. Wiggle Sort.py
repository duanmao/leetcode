class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        less = True
        for i in range(len(nums) - 1):
            if (less and nums[i] > nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
            elif (not less and nums[i] < nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
            less = not less
