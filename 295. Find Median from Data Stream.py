# Time: add O(nlogn), find O(1)
# Space: O(n)
from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = [] # maxheap
        self.large = [] # minheap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if (len(self.small) == len(self.large)):
            heappush(self.large, num)
            heappush(self.small, -heappop(self.large))
        else:
            heappush(self.small, -num)
            heappush(self.large, -heappop(self.small))

    def findMedian(self):
        """
        :rtype: float
        """
        # print("m", self.small[0], self.large[0])
        if (len(self.small) == len(self.large)):
            return (-self.small[0] + self.large[0]) / 2.0
        else:
            return -self.small[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
