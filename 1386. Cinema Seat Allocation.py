# Time: O(n), space: O(n)
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        candidates = [{2,3,4,5}, {4,5,6,7}, {6,7,8,9}]

        rows = collections.defaultdict(list)
        for r, s in reservedSeats: rows[r].append(s)
        count = (n - len(rows)) * 2 # 2 families can be allocated in empty rows
        for occupied in rows.values():
            allocs = [1, 1, 1]
            for s in occupied:
                for i, c in enumerate(candidates):
                    if s in c: allocs[i] = 0
            # 4567 will become invalid if either 2345 or 6789 is taken
            if allocs[0] or allocs[2]: allocs[1] = 0
            count += sum(allocs)
        return count

# Time: O(nlogn), space: O(1)
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        def allocSameRow(s1, s2):
            if s2 - s1 >= 9: 
                if s1 >= 2 or s2 <= 9: return 1
                else: return 2
            elif s2 - s1 >= 5 and (s1, s2) not in {(0, 5), (2, 7), (4, 9), (6, 11)}:
                return 1
            return 0
            
        reservedSeats.sort()
        count = (reservedSeats[0][0] - 1) * 2 + allocSameRow(0, reservedSeats[0][1])
        for i in range(1, len(reservedSeats)):
            prow, pseat = reservedSeats[i - 1]
            crow, cseat = reservedSeats[i]
            if prow == crow:
                count += allocSameRow(pseat, cseat)
            else:
                count += allocSameRow(pseat, 11) + 2 * (crow - prow - 1) + allocSameRow(0, cseat)
        count += allocSameRow(reservedSeats[-1][1], 11) + (n - reservedSeats[-1][0]) * 2
        return count
