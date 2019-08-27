# Time: O(n!) where n is maximum pattern length
# Space: O(n), where n is maximum pattern length. In the worst case the maximum depth of recursion is n. Therefore we need O(n) space used by the system recursive stack
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        
        def legal(keys, pending):
            if (not keys): return True
            last = keys[-1]
            if (last // 3 == pending // 3):
                if (abs(last - pending) == 2):
                    if (min(last, pending) + 1 not in keys): return False
            if (last % 3 == pending % 3):
                if (abs(last - pending) == 6):
                    if (min(last, pending) + 3 not in keys): return False
            if (abs(last - pending) == 8 or 
                (abs(last - pending) == 4 and min(last, pending) == 2)):
                if (4 not in keys): return False
            return True
        
        def count(keys, nkeys):
            if (len(keys) == nkeys):
                self.counts[keys[0]] += 1
                return
            for i in range(9):
                # 0 1 2
                # 3 4 5
                # 6 7 8
                # basically we only need to calculate combinations starting from 0, 1 and 4
                # because 0, 2, 6, 8 are symmetric, and 1, 3, 5, 7 are symmetric
                if (not keys and i > 1 and i != 4): continue # symmetry, skip them
                if (i not in keys and legal(keys, i)):
                    keys.append(i)
                    count(keys, nkeys)
                    keys.pop()
            
        total = 0
        for i in range(m, n + 1):
            self.counts = [0] * 5
            count([], i)
            total += (self.counts[0] + self.counts[1]) * 4 + self.counts[4]
        return total
