# https://leetcode.com/problems/best-meeting-point/discuss/74193/Java-2msPython-40ms-two-pointers-solution-no-median-no-sort-with-explanation 
# Time: O(mn), space: O(m + n)
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # choose median as the meeting point will give the minimal distance,
        # thus we want to find the median with regard to row and column respectively
        
        if (not grid): return 0
        m, n = len(grid), len(grid[0])
        
        rows, cols = [0] * m, [0] * n
        # collecting the coordinates in this way to avoid sorting them
        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
              
        def distance(seqs):
            dist = 0
            # two pointers moving towards the median from ends, because the final answer may be
            # one of the ends, we need to start from outside so that we can initialize 
            # left and right below all to be 0; otherwise, see comments as alternative
            meetl, meetr = -1, len(seqs) # 0, len(seqs) - 1
            # how many people the two pointers have passed so far (!!!inclusive), respectively
            left = right = 0 # left, right = seqs[meetl], seqs[meetr]
            # our aim is to find the median and calculate the distance along the way
            # to find the median, our target is meetl == meetr, and by definition,
            # median is the number that separate left and right equally
            # to compute distance simultaneously, note that everytime we move the left pointer +1
            # or the right pointer -1, the total distance will increase by the number of people
            # alreasy passed by this pointer, because they're one step further
            while (meetl != meetr):
                if (left < right): # move left pointer so that there'll be more people on the left
                    dist += left
                    meetl += 1
                    left += seqs[meetl]
                else:
                    dist += right
                    meetr -= 1
                    right += seqs[meetr]
            return dist
        
        return distance(rows) + distance(cols)

# https://leetcode.com/problems/best-meeting-point/solution/
# As long as there is equal number of points to the left and right of the meeting point, the total distance is minimized.
# "the median minimizes the sum of absolute deviationsi"
# for more theory on this:
# https://leetcode.com/problems/best-meeting-point/discuss/74189/Am-I-the-only-person-who-don't-know-why-median-could-give-shortest-distance
# Time: O(mn), space: O(mn) worst case
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # choose median as the meeting point will give the minimal distance,
        # thus we want to find the median with regard to row and column respectively
        
        if (not grid): return 0
        m, n = len(grid), len(grid[0])
        
        rows, cols = [], []
        # collecting the coordinates in this way to avoid sorting them
        for i in range(m):
            for j in range(n):
                if (grid[i][j]): rows.append(i)
        for j in range(n):
            for i in range(m):
                if (grid[i][j]): cols.append(j)
              
        def distance(seqs):
            dist = 0
            left, right = 0, len(seqs) - 1
            while (left < right):
                dist += seqs[right] - seqs[left]
                left += 1
                right -= 1
            return dist
        
        return distance(rows) + distance(cols)
