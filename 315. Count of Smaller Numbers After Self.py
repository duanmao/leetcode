# Time: O(nlogn), space: O(n)
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        smaller = [0] * len(nums)

        def mergesort(enums):
            if len(enums) <= 1: return enums
            mid = len(enums) // 2
            left = mergesort(enums[:mid])
            right = mergesort(enums[mid:])
            for i in range(len(enums))[::-1]:
                if not right or (left and left[-1][1] > right[-1][1]):
                    smaller[left[-1][0]] += len(right)
                    enums[i] = left.pop()
                else:
                    enums[i] = right.pop()
            return enums

        mergesort(list(enumerate(nums)))
        return smaller
