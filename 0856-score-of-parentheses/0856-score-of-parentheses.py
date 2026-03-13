class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        scores = [0]
        for p in s:
            if p == '(':
                scores.append(0)
            else:
                popped = scores.pop()
                if stack[-1] == '(':
                    scores[-1] += popped + 1
                else:
                    scores[-1] += popped * 2
            stack.append(p)
        return scores[0]

# optimization
# we can do it with O(1) space 
# class Solution:
#     def scoreOfParentheses(self, s: str) -> int:
#         n = len(s)
#         score = 0
#         depth = 0 

#         for i in range(n):
#             if s[i] == '(':
#                 depth += 1
#             else:
#                 if s[i-1] == '(':
#                     depth -= 1
#                     score += 2 ** depth
#                 else:
#                     depth -= 1
                    
#         return score
        
