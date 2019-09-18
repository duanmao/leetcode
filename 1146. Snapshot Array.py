# https://leetcode.com/problems/snapshot-array/discuss/350562/JavaPython-Binary-Search
class SnapshotArray:

    # O(n)
    def __init__(self, length: int):
        self.nextid = 0
        self.history = [[(-1, 0)] for i in range(length)]

    # O(1)
    def set(self, index: int, val: int) -> None:
        self.history[index].append((self.nextid, val))

    # O(1)
    def snap(self) -> int:
        self.nextid += 1
        return self.nextid - 1

    # O(logk)
    def get(self, index: int, snap_id: int) -> int:
        if (snap_id >= self.nextid): return float('-inf')
        idx = bisect.bisect(self.history[index], (snap_id, float('inf'))) - 1
        return self.history[index][idx][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
