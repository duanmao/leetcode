# Time: O(n^2), space: O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if (i and nums[i] == nums[i - 1]):
                continue
            left = i + 1
            right = n - 1
            while (left < right):
                sm = nums[i] + nums[left] + nums[right]
                if (sm == 0):
                    res.append([nums[i], nums[left], nums[right]])
                    while (left < right and nums[left] == nums[left + 1]):
                        left += 1
                    while (left < right and nums[right] == nums[right - 1]):
                        right -= 1
                    left += 1
                    right -= 1
                elif (sm < 0):
                    left += 1
                else:
                    right -= 1
                
        return res
