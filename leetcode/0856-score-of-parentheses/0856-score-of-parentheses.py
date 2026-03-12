class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        score = 0
        depth = 0 

        for i in range(n):
            if s[i] == '(':
                depth += 1
            else:
                if s[i-1] == '(':
                    depth -= 1
                    score += 2 ** depth
                else:
                    depth -= 1
                    
        return score
