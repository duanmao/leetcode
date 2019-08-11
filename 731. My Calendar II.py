class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.overlaps = []

    # for 2 time intervals [s1, e1) [s2, e2) to have no collision:
    # s1 >= e2 || s2 >= e1
    # thus for them to have collision: !(s1 >= e2 || s2 >= e1) ->
    # s1 < e2 && s2 < e1
    # if time intervals are given by [s1, e1] [s2, e2] then it becomes:
    # s1 <= e2 && s2 <= e1 to collide
    def __collide(self, interval1, interval2):
        s1, e1 = interval1
        s2, e2 = interval2
        return s1 < e2 and s2 < e1
        
    def book(self, start: int, end: int) -> bool:
        for overlap in self.overlaps:
            if (self.__collide(overlap, (start, end))): return False
            
        for s, e in self.events:
            if (self.__collide((s, e), (start, end))):
                self.overlaps.append((max(s, start), min(e, end)))
        self.events.append([start, end])
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
