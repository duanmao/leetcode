class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numidx = [(nums[i], i) for i in range(len(nums))]
        numidx.sort()
        left, right = 0, len(numidx) - 1
        while (left < right):
            s = numidx[left][0] + numidx[right][0]
            if (s == target):
                return [numidx[left][1], numidx[right][1]]
            elif (s < target):
                left += 1
            else:
                right -= 1
        return []
