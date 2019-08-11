class MyCalendarThree:

    def __init__(self):
        self.delta = collections.Counter()

    # O(nlogn), but a sorted map (like map in C++) can reduce it to O(N)
    # https://leetcode.com/problems/my-calendar-iii/discuss/109556/JavaC%2B%2B-Clean-Code
    def book(self, start: int, end: int) -> int:
        self.delta[start] += 1
        self.delta[end] -= 1

        active = res = 0
        for x in sorted(self.delta):
            active += self.delta[x]
            res = max(res, active)

        return res


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
