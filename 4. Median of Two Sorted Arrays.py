# Time: O(log(m + n)), space: O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def kthSmallest(nums1, l1, h1, nums2, l2, h2, k):
            # A[0, i - 1] contains i nums, B[0, j - 1] contains j nums
            # assume i + j = k - 1 so that the next number after A[i - 1] and B[j - 1]
            # could be our target: the kth smallest num
            i = math.floor((h1 - l1 + 1) / (h1 - l1 + 1 + h2 - l2 + 1) * (k - 1))
            j = k - 1 - i
            i += l1
            j += l2
            Ai_1 = float('-inf') if i - 1 < 0 else nums1[i - 1]
            Ai = float('inf') if i > h1 else nums1[i]
            Bj_1 = float('-inf') if j - 1 < 0 else nums2[j - 1]
            Bj = float('inf') if j > h2 else nums2[j]
            
            if (Bj_1 <= Ai <= Bj):
                return Ai
            elif (Ai_1 <= Bj <= Ai):
                return Bj
            elif (Ai < Bj): 
                # essentially A[i] < B[j-1], discard left part of A since they are too small
                # similarly discard right part of B since they are too big
                return kthSmallest(nums1, i + 1, h1, nums2, l2, j - 1, k - (i - l1 + 1))
            else:
                # essentially B[j] < A[i-1], ditto
                return kthSmallest(nums1, l1, i - 1, nums2, j + 1, h2, k - (j - l2 + 1))
        
        m = len(nums1)
        n = len(nums2)
        if ((m + n) % 2):
            return kthSmallest(nums1, 0, m - 1, nums2, 0, n - 1, (m + n) // 2 + 1)
        else:
            med1 = kthSmallest(nums1, 0, m - 1, nums2, 0, n - 1, (m + n) // 2)
            med2 = kthSmallest(nums1, 0, m - 1, nums2, 0, n - 1, (m + n) // 2 + 1)
            return (med1 + med2) / 2
