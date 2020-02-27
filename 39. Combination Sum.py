# Time: O(k * 2 ^ n'), k: average length of each solution, n': longer than len(cands)
# Time analysis: https://github.com/Deadbeef-ECE/Interview/blob/master/Leetcode/BackTracking/039_Combination_Sum.java
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def combination(idx, cur, cursum):
            if cursum == target:
                res.append(cur)
                return
            for i in range(idx, len(candidates)):
                add = cursum + candidates[i]
                if add <= target:
                    combination(i, cur + [candidates[i]], add)
                else:
                    break

        combination(0, [], 0)
        return res
