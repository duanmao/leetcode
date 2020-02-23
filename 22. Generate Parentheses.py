class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parens = []
        
        def generate(left, right, cur):
            if right == 0:
                parens.append(cur)
                return
            if left: generate(left - 1, right, cur + '(')
            if left < right: generate(left, right - 1, cur + ')')
                    
        generate(n, n, "")
        return parens
