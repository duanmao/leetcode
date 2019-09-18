# Time: O(logn) where n is the length of the array, though it's unknown to us
class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        high = 1
        while (reader.get(high) < target):
            high <<= 1
        low = high >> 1
        while (low <= high):
            mid = (low + high) // 2
            num = reader.get(mid)
            if (num == target): return mid
            elif (num < target): low = mid + 1
            else: high = mid - 1
        return -1
