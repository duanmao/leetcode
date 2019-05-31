# 在看了别的答案后，这个方法对于处理这题来说明显是overkill了
# 更适合这题的方法见C++
# 维护两个指针，均从左往右，第一个先走，寻找为零的元素
# 当找到一个0后，第二个从自己所在的位置继续往下走，寻找不为零的元素
# 然后将两者所在位置的元素进行互换，再将两个指针都往后移一位
# 直到第二个指针走到头为止
# 时间复杂度：O(n)，空间复杂度：O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        nonzero = 0
        n = len(nums)
        while (nonzero < n):
            while (zero < n and nums[zero] != 0):
                zero += 1
            if (nonzero < zero): # ATTENTION! This does MUCH MORE than an optimization
                nonzero = zero + 1 # It actually is indispensable here for certain cases
            while (nonzero < n and nums[nonzero] == 0):
                nonzero += 1
            if (zero < n and nonzero < n):
                nums[zero], nums[nonzero] = nums[nonzero], nums[zero]
                zero += 1
                nonzero += 1
