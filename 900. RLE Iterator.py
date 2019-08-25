# Time: O(n)
class RLEIterator:

    def __init__(self, A: List[int]):
        self.data = A
        self.ptr = 0
        self.used = 0

    def next(self, n: int) -> int:
        while (self.ptr < len(self.data)):
            if (n <= self.data[self.ptr] - self.used):
                self.used += n
                return self.data[self.ptr + 1]
            else:
                n -= (self.data[self.ptr] - self.used)
                self.used = 0
                self.ptr += 2
        return -1
        

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
