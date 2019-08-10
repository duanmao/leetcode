# Time: O(n), space: O(n)
# space O(1) solution exists.. but...
# https://leetcode.com/problems/fruit-into-baskets/discuss/170745/Problem%3A-Longest-Subarray-With-2-Elements
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        total = start = 0
        collected = collections.defaultdict(int)
        counter = 0
        for i, tp in enumerate(tree):
            if (not collected[tp]): counter += 1
            collected[tp] += 1
            while (counter > 2):
                collected[tree[start]] -= 1
                if (not collected[tree[start]]): 
                    counter -= 1
                    del collected[tree[start]] # not sure whether space can be considered as O(1)
                start += 1
            total = max(total, i - start + 1)
        return total
