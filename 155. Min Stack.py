class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackNorm = []
        self.stackMin = []

    def push(self, x: int) -> None:
        self.stackNorm.append(x)
        if (not len(self.stackMin) or x <= self.getMin()):
            self.stackMin.append(x)

    def pop(self) -> None:
        if (self.top() == self.getMin()):
            self.stackMin.pop()
        self.stackNorm.pop()

    def top(self) -> int:
        return self.stackNorm[-1]

    def getMin(self) -> int:
        return self.stackMin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
