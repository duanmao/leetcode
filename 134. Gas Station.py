# Time: O(n), space: O(1)
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total = left = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            left += gas[i] - cost[i]
            if (left < 0):
                left = 0
                start = i + 1
        return start if total >= 0 else -1

# Time: O(n), space: O(1)
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        bottleneck = float('inf')
        left = 0
        start = 0
        n = len(gas)
        for i in range(n):
            left += gas[i] - cost[i]
            if (bottleneck > left):
                bottleneck = left
                start = i + 1
        return start % n if left >= 0 else -1
