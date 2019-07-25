# Time: O(n), space: O(1)
# split the elements into 3 piles, small, median, large
# large will fill in the odd slots from the beginning
# small will fill in the even slots back from the end
# median will fill in the rest of the slots
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def nthElement(low, high, n):
            mx = max(nums)
            mn = min(nums)
            if (mx - mn <= 10): # to bypass certain large OJ cases
                bucket = [0] * (mx - mn + 1)
                for num in nums:
                    bucket[num - mn] += 1
                total = 0
                for i in range(len(bucket)):
                    total += bucket[i]
                    if (total >= n):
                        return i + mn
            
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
        n = len(nums)
        # +1 here to find a "larger median" because the slots for larger elements are always lte the
        # slots for smaller ones, since it starts later. Thus, we must ensure we have less larger
        # elements than the median, otherwise the index may grow out of range at line 57
        median = nthElement(0, n - 1, n // 2 + 1)
        cur = -1
        large = 1
        small = (n - 1) // 2 * 2
        while (cur < n - 1): # cur is moved forward right after entering the loop, thus must -1 here
            cur += 1
            # print(cur, large, small)
            # print(nums)
            if (nums[cur] > median):
                if (cur <= large and cur % 2): # skip elements already handled
                    continue
                nums[cur], nums[large] = nums[large], nums[cur]
                cur -= 1
                large += 2
            elif (nums[cur] < median):
                if (cur >= small and cur % 2 == 0): # skip elements already handled
                    continue
                nums[cur], nums[small] = nums[small], nums[cur]
                cur -= 1
                small -= 2

# Time: O(nlogn), space: O(n)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cp = sorted(nums)
        n = len(nums)
        for i in range(1, n, 2):
            nums[i] = cp.pop()
        for i in range(0, n, 2):
            nums[i] = cp.pop()
