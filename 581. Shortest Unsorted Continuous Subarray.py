# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solution/

# Time: O(n) (4n though), space: O(1)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        MIN, MAX = float('inf'), float('-inf')
        n = len(nums)
        for i, num in enumerate(nums):
            if i and nums[i - 1] > num:
                MIN = min(MIN, num)
        for i in reversed(range(n - 1)):
            if nums[i] > nums[i + 1]:
                MAX = max(MAX, nums[i])
        left = right = -1
        for i, num in enumerate(nums):
            if num > MIN:
                left = i
                break
        for i in reversed(range(n)):
            if nums[i] < MAX:
                right = i
                break
        return right - left + 1 if right > left else 0

# Time: O(n), space: O(n)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        left, right = n, -1
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                left = min(left, stack.pop())
            stack.append(i)
        stack = []
        for i in reversed(range(n)):
            while stack and nums[stack[-1]] < nums[i]:
                right = max(right, stack.pop())
            stack.append(i)
        return right - left + 1 if right > left else 0

# Time: O(nlogn), space: O(n)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = right = -1
        srtnums = sorted(nums)
        for i in range(n):
            if srtnums[i] != nums[i]:
                if left == -1: left = i
                if right < i: right = i
        return right - left + 1 if right > left else 0
