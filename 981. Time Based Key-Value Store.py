class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        return self.__binarysearch(self.store[key], timestamp)

    # can use built-in bisect like in this:
    # https://leetcode.com/problems/time-based-key-value-store/discuss/247130/Python-concise-6-liner
    def __binarysearch(self, tvs, time):
        low, high = 0, len(tvs) - 1
        while (low <= high):
            mid = (low + high) // 2
            t, v = tvs[mid]
            if (t <= time): low = mid + 1
            else: high = mid - 1
        return tvs[high][1] if high >= 0 else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
