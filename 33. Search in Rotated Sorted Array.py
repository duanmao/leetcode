# Time: O(logn), space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while (low <= high):
            mid = int((low + high) / 2)
            if (nums[mid] == target):
                return mid
            elif (nums[mid] < target):
                # 若数组是正常的排序数组，这时的正常操作是low = mid + 1
                # 因此只要判断因数组被移动而导致的不得不向左边查找的例外情况即可
                # 而这种例外只出现在一种情境下：
                # 当nums[mid]落在移动后较小的后半段而target应在较大的前半段时
                # 除此之外都应当循例往右边查找
                # 为了限制nums[mid]在后半段，则它必须 < nums[low]
                # 而为了限制target在前半段，它必须 > nums[high]
                # 当然同时还必须保证low到high的范围是被移动过的，即nums[low] > nums[high]
                # 但上述两个判断条件中已隐含此判断，所以不需要再作显式判断
                # 另：可能感觉上 nums[mid] < nums[low] 等价于 nums[mid] <= nums[high]
                # 以及 target > nums[high] 等价于 target >= nums[low]
                # 但当两个条件都允许等于时出现的问题正是无法确保low到high是被移动过的
                # 因为若要用这两条来做判断，则必须再加上nums[low] > nums[high]来保证偏序关系
                # 即 if (nums[mid] <= nums[high] and target >= nums[low] and nums[low] > nums[high])
                # 因此，更建议使用严格的大于小于来做判断，即如下：
                if (nums[mid] < nums[low] and target > nums[high]):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # 若数组是正常的排序数组，这时的正常操作是high = mid - 1
                # 因此只要判断因数组被移动而导致的不得不向右边查找的例外情况即可
                # 而这种例外只出现在一种情境下：
                # 当nums[mid]落在移动后较大的前半段而target应在较小的后半段时
                # 除此之外都应当循例往左边查找
                # 为了限制nums[mid]在前半段，则它必须 > nums[high]
                # 而为了限制target在后半段，它必须 < nums[low]
                # 当然同时还必须保证low到high的范围是被移动过的，即nums[low] > nums[high]
                # 但上述两个判断条件中已隐含此判断，所以不需要再作显式判断
                # 另：大致同上
                if (nums[mid] > nums[high] and target < nums[low]):
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
