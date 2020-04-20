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

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.min = float('inf')

    def push(self, x: int) -> None:
        self.min = min(self.min, x)
        self.s.append((x, self.min))

    def pop(self) -> None:
        self.s.pop()
        # ****** MUST UPDATE the current MIN !!! ******
        self.min = max(self.min, self.s[-1][1] if self.s else float('inf'))

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
