# Time: O(n), space: O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
            
        i = 0
        while (i < len(nums)):
            if (nums[nums[i] - 1] != nums[i]):
                swap(nums[i] - 1, i)
            else:
                i += 1
        return [i + 1 for i, num in enumerate(nums) if num != i + 1]
