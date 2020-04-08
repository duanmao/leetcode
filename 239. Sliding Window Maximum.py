# Time: O(n), space: O(k)
# https://leetcode.com/problems/sliding-window-maximum/discuss/65884/Java-O(n)-solution-using-deque-with-explanation
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque() # must store index instead of its value
        for i, num in enumerate(nums):
            # check whether the leftmost element still stays inside the window or not
            # if it has been slided out, it should be removed
            if dq and dq[0] <= i - k: dq.popleft()
            # check whether the numbers come later are promising to be the max in the window or not
            # if they are smaller than the element that we're going to add, they are impossible to
            # be selected as the maximum within the window since this current element num[i] would
            # always overshadow them. Thus they should be removed
            while dq and nums[dq[-1]] <= nums[i]: dq.pop()
            dq.append(i)
            # since the promising numbers are stored sequentially according to their relative order
            # in the given array, and in descending order in terms of their values, the first
            # element must be the correct choice for the current window
            if i >= k - 1: res.append(nums[dq[0]])
        return res

# Time: O(n), space: O(k)
# monotonic queue implementation
from collections import deque

class MonoQueue:
    def __init__(self):
        self.dq = deque()
        
    def push(self, val):
        count = 1
        while (len(self.dq) and self.dq[-1][0] <= val):
            count += self.dq[-1][1]
            self.dq.pop()
        self.dq.append([val, count])
        
    def pop(self):
        if (len(self.dq)):
            self.dq[0][1] -= 1
            if (self.dq[0][1] <= 0):
                self.dq.popleft()
    
    def top(self):
        return self.dq[0][0] if len(self.dq) else 0

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if (not k): return []
        if (k >= len(nums)): return [max(nums)]
        mq = MonoQueue()
        for i in range(k - 1): mq.push(nums[i])
        res = []
        for i in range(k - 1, len(nums)):
            mq.push(nums[i])
            res.append(mq.top())
            mq.pop()
        return res
