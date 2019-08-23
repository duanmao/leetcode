# Time: O(1)
# Using circular array
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.nums = [0] * size
        self.size = size
        self.sum = 0
        self.n = 0
        
    def next(self, val: int) -> float:
        # don't even need to do the size check before deduction since nums are initialized to be 0
        self.sum -= self.nums[self.n % self.size]
        self.nums[self.n % self.size] = val
        self.sum += val
        self.n += 1
        return self.sum / min(self.n, self.size)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# Using deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.nums = collections.deque()
        self.size = size
        self.sum = 0
        
    def next(self, val: int) -> float:
        self.nums.append(val)
        self.sum += val
        if (len(self.nums) > self.size):
            self.sum -= self.nums.popleft()
        return self.sum / len(self.nums)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
