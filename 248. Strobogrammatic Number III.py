class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        mapping = {('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')}
        
        def countForLenLessThan(cur, left, right, limit, include):
            if (left > right):
                stro = "".join(cur)
                if (stro < limit): self.sameLenCount += 1
                elif (include and stro == limit): self.sameLenCount += 1
                return
            for c1, c2 in mapping:
                if (left == 0 and right != 0 and c1 == '0'): continue
                if (left == right and c1 in {'6', '9'}): continue
                cur[left] = c1
                cur[right] = c2
                countForLenLessThan(cur, left + 1, right - 1, limit, include)
        
        def countForLen(length):
            if (length == 0): return 0
            if (length == 1): return 3
            if (length % 2):
                return 4 * (5 ** (length // 2 - 1)) * 3
            else:
                return 4 * (5 ** (length // 2 - 1))
            
        def count(num, include = True):
            shorterCount = 0
            for l in range(1, len(num)):
                shorterCount += countForLen(l)
                
            self.sameLenCount = 0
            countForLenLessThan([""] * len(num), 0, len(num) - 1, num, include)
            return shorterCount + self.sameLenCount
        
        if (len(low) > len(high) or (len(low) == len(high) and low > high)):
            return 0
        chigh, clow = count(high), count(low, False)
        return chigh - clow

# slower, but certainly shorter and easier
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        mapping = {('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')}
        
        self.total = 0
        def generate(cur, left, right):
            if (left > right):
                stro = "".join(cur)
                if ((len(stro) == len(low) and stro < low) or
                    (len(stro) == len(high) and stro > high)): return
                self.total += 1
                return
            for c1, c2 in mapping:
                if (left == right and c1 in {'6', '9'}): continue
                elif (left == 0 and right != 0 and c1 == '0'): continue
                cur[left] = c1
                cur[right] = c2
                generate(cur, left + 1, right - 1)
                
        for l in range(len(low), len(high) + 1):
            generate([""] * l, 0, l - 1)
        return self.total
