# Time: O(n), space: O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def nthElement(low, high, n):
            def split(low, high): # return split index
                ptr = low
                for i in range(low + 1, high + 1):
                    if (nums[i] < nums[low]):
                        ptr += 1
                        nums[i], nums[ptr] = nums[ptr], nums[i]
                nums[ptr], nums[low] = nums[low], nums[ptr]
                return ptr
            
            while (low <= high):
                idx = split(low, high)
                if (idx == n - 1):
                    return nums[idx]
                elif (idx < n - 1):
                    low = idx + 1
                else:
                    high = idx - 1
            return nums[n - 1]
        
        random.shuffle(nums)
        return nthElement(0, len(nums) - 1, len(nums) - k + 1)
