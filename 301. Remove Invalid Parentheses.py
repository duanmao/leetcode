# https://leetcode.com/problems/remove-invalid-parentheses/discuss/75027/Easy-Short-Concise-and-Fast-Java-DFS-3-ms-solution
# This is hard to understand.. specifically the duplicate removal logic. So in real interview,
# But it is indeed the fastest solution among the all
# however for me, probably just using a set to remove the duplicates is a more feasible option
# since it's almost impossible for me to implement it as below without referencing the exisiting code
# Time: O(nm) where m is the total "number of recursive calls" or "nodes in the search tree". 
# So worst case: O(n^2)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def dfs(s, lasti, lastj, res, matches):
            counter = 0
            for i in range(lasti, len(s)):
                if (s[i] == matches[0]): counter += 1
                elif (s[i] == matches[1]): counter -= 1
                if (counter >= 0): continue
                for j in range(lastj, i + 1):
                    if (s[j] == matches[1] and 
                        ((j == lastj or not s[j] == s[j - 1]))):
                        dfs(s[:j] + s[j + 1:], i, j, res, matches)
                return
            if (matches[0] == '('): # finished left to right: removed excessive ')'
                dfs(s[::-1], 0, 0, res, [')', '('])
            else: # finished both sides: removed both excessive ')' and '('
                res.append(s[::-1])
            
        res = []
        dfs(s, 0, 0, res, ['(', ')'])
        return res

# Time: worst O(2^n)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def dfs(s, res, matches):
            counter = 0
            for i in range(len(s)):
                if (s[i] == matches[0]): counter += 1
                elif (s[i] == matches[1]): counter -= 1
                if (counter >= 0): continue
                for j in range(i + 1):
                    if (s[j] == matches[1]):
                        dfs(s[:j] + s[j + 1:], res, matches)
                return
            if (matches[0] == '('):
                dfs(s[::-1], res, [')', '('])
            else:
                res.add(s[::-1])
            
        res = set()
        dfs(s, res, ['(', ')'])
        return res
