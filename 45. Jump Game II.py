# Time: O(n), space: O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        cur = far = 0
        n = len(nums)
        while (cur <= far and far < n - 1):
            step += 1
            for i in range(cur, far + 1):
                far = max(far, i + nums[i])
            cur = i + 1
        return step if far >= n - 1 else -1
