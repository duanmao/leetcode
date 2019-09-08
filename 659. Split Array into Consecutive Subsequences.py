# https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/106495/Java-O(n)-time-and-O(1)-space-solution-greedily-extending-shorter-subsequence
# Time: O(n), space: O(1)
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        pre = None
        # counting subsequences of length 1, 2, and 3+ that ends at an element
        l1 = l2 = lm = 0
        count = 1 # frequency of a number
        for i, num in enumerate(nums):
            if (i < len(nums) - 1 and num == nums[i + 1]):
                count += 1
                continue
            if (pre == None or num != pre + 1):
                # current number must start new subsequences
                if (l1 != 0 or l2 != 0): return False
                l1 = count
                l2 = lm = 0
            else: # current number can be appended to existing subsequences
                # its frequency must at least satisfy subsequences of length 1 and 2
                if (count < l1 + l2): return False
                p1, p2, pm = l1, l2, lm
                l2 = p1
                lm = p2 + min(pm, count - (p1 + p2))
                l1 = max(0, count - (p1 + p2 + pm))
            count = 1
            pre = num
        return l1 == l2 == 0

# https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/106514/Python-esay-understand-solution
# Time: O(n), space: O(n)
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        avail = collections.Counter(nums)
        end = collections.defaultdict(int)
        for num in nums:
            if (not avail[num]): continue
            avail[num] -= 1
            if (end.get(num - 1)): # append to existing subsequences
                end[num - 1] -= 1
                end[num] += 1
            else: # have to start new sequences
                if (not avail.get(num + 1) or not avail.get(num + 2)): return False
                avail[num + 1] -= 1
                avail[num + 2] -= 1
                end[num + 2] += 1
        return True

# 3rd solution
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/106538/Python-O(N)-Straightforward-Solution
