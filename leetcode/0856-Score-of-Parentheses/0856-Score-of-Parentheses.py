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