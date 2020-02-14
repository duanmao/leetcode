class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.v = v
        self.ptr1 = self.ptr2 = 0

    def next(self) -> int:
        if self.hasNext():
            res = self.v[self.ptr1][self.ptr2]
            self.ptr2 += 1
            return res
        else:
            return None

    def hasNext(self) -> bool:
        if self.ptr1 >= len(self.v): return False
        if self.ptr2 < len(self.v[self.ptr1]): return True
        self.ptr2 = 0
        self.ptr1 += 1
        while self.ptr1 < len(self.v) and not self.v[self.ptr1]:
            self.ptr1 += 1
        return self.ptr1 < len(self.v)

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
