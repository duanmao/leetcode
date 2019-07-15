# Time: O(nlogn), space: O(n)
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergesort(enum):
            mid = math.floor(len(enum) / 2)
            if (mid):
                left = mergesort(enum[:mid])
                right = mergesort(enum[mid:])
                for i in range(len(enum))[::-1]:
                    if (not right or (left and left[-1][1] > right[-1][1])):
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        
        smaller = [0] * len(nums)
        mergesort(list(enumerate(nums)))
        return smaller
