# Same as one solution to meeting rooms III
# Track the change of number of passengers in time order.
# O(nlogn), space: O(n)
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = [(s, p) for p, s, e in trips]
        changes.extend([(e, -p) for p, s, e in trips])
        changes.sort()
        carry = 0
        for time, change in changes:
            carry += change
            if (carry > capacity):
                return False
        return True

# Similar to one solution of meeting rooms II, but slightly different
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        picks = sorted([(s, p) for p, s, e in trips])
        offs = sorted([(e, p) for p, s, e in trips])
        carry = 0
        ptr_o = 0
        for p_time, psg in picks:
            while (p_time >= offs[ptr_o][0]): # drop off clients of the last trip
                carry -= offs[ptr_o][1]
                ptr_o += 1
            # pick up clients of this trip
            carry += psg
            if (carry > capacity):
                return False
        return True
