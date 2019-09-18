# https://leetcode.com/problems/candy/discuss/42770/One-pass-constant-space-Java-solution/162756
# Time: O(n), space: O(1)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = 0
        valley = peak = 0
        while (valley < n - 1): # note n - 1 here instead of n, otherwise this loop will never end
            lastv = valley
            peak = valley
            while (peak < n - 1 and ratings[peak] < ratings[peak + 1]): peak += 1
            valley = peak
            while (valley < n - 1 and ratings[valley] > ratings[valley + 1]): valley += 1
            longslope = max(peak - lastv, valley - peak) + 1
            shortslope = min(peak - lastv, valley - peak) # the peak is already inlcuded in longslope
            candies += (1 + longslope) * longslope // 2
            candies += (1 + shortslope) * shortslope // 2
            while (valley < n - 1 and ratings[valley] == ratings[valley + 1]):
                valley += 1
                candies += 1 # it's so unfair that children who have the same ratings as their neighbors only get 1 candies while the neighbors may get more if they have lower-rating neighbors, makes no sense, but it's what the problem defines
            candies -= 1 # deduct the last 1 candy since it will be re-counted in the next peak-valley detection
        return candies + 1


# Time: O(3n), or O(2n) if candies are summed up within the 2nd update loop, space: O(n)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if (ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]):
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if (ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]):
                candies[i] = candies[i + 1] + 1
        return sum(candies)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if (ratings[i] > ratings[i - 1]):
                candies[i] = max(candies[i], candies[i - 1] + 1)
        for i in range(n - 2, -1, -1):
            if (ratings[i] > ratings[i + 1]):
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)
