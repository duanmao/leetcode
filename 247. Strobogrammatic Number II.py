# Time: O(5^n)
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        pairs = {'6':'9','9':'6','8':'8','1':'1','0':'0'}
        singles = ['0', '1', '8']
        
        def generate(res, cur, n):
            if (len(cur) == n):
                res.append(cur)
            else:
                for k in pairs:
                    if (len(cur) == n - 2 and k == '0'): continue
                    generate(res, k + cur + pairs[k], n)
            
        res = []
        if (n % 2):
            for c in singles:
                generate(res, c, n)
        else:
            generate(res, "", n)
        return res
