# https://leetcode.com/problems/meeting-rooms-ii/solution/
# Time: O(nlogn), space: O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([s for s, e in intervals])
        ends = sorted([e for s, e in intervals])
        e_ptr = 0
        rooms = 0
        for s in starts:
            if (ends[e_ptr] <= s):
                rooms -= 1 # free one room
                e_ptr += 1
            rooms += 1 # open a room for the current meeting
        return rooms

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([s for s, e in intervals])
        ends = sorted([e for s, e in intervals])
        e_ptr = 0
        rooms = 0
        for s in starts:
            if (ends[e_ptr] <= s): # we have a free room just give to the current meeting
                e_ptr += 1
            else:
                rooms += 1 # we need to open a new room
        return rooms

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if (not intervals): return 0

        intervals.sort()

        # Add the first meeting. We have to give a new room to the first meeting.
        rooms = [intervals[0][1]] # end time

        # For all the remaining meeting rooms
        for meeting in intervals[1:]:
            # If a meeting has ended before the current meeting starts, free that room
            if (rooms[0] <= meeting[0]):
                heapq.heappop(rooms)

            # Assign a room to the current meeting
            heapq.heappush(rooms, meeting[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(rooms)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([s for s, e in intervals])
        ends = sorted([e for s, e in intervals])
        ptrS = ptrE = 0
        rooms = avail = 0
        while (ptrS < len(starts)):
            if (starts[ptrS] < ends[ptrE]):
                # a meeting starts before another ends, we need another room
                if (not avail): rooms += 1
                else: avail -= 1
                ptrS += 1
            else:
                # a meeting ended before another starts, we have a vacant room
                avail += 1
                ptrE += 1
        return rooms

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([s for s, e in intervals])
        ends = sorted([e for s, e in intervals])
        ptrS = ptrE = 0
        rooms = need = 0
        while (ptrS < len(starts)):
            if (starts[ptrS] < ends[ptrE]):
                # a meeting starts before another ends, we need another room
                need += 1
                ptrS += 1
            else:
                # a meeting ended before another starts, we have a vacant room
                need -= 1
                ptrE += 1
            rooms = max(rooms, need)
        return rooms
