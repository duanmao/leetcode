# Time: O(n), space: O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = m - 1
        ptr2 = n - 1
        ptr = m + n - 1
        while (ptr2 >= 0 and ptr1 >= 0):
            if (nums2[ptr2] >= nums1[ptr1]):
                nums1[ptr] = nums2[ptr2]
                ptr2 -= 1
            else:
                nums1[ptr] = nums1[ptr1]
                ptr1 -= 1
            ptr -= 1
        while (ptr2 >= 0):
            nums1[ptr] = nums2[ptr2]
            ptr2 -= 1
            ptr -= 1

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = m - 1
        ptr2 = n - 1
        ptr = m + n - 1
        while (ptr2 >= 0 and ptr >= 0): # both ptr2 and ptr need to be checked
            if (ptr1 < 0 or nums2[ptr2] >= nums1[ptr1]): # check ptr1 here
                nums1[ptr] = nums2[ptr2]
                ptr2 -= 1
            else:
                nums1[ptr] = nums1[ptr1]
                ptr1 -= 1
            ptr -= 1
