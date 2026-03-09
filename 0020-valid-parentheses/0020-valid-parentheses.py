class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        D = {'(':')','{':'}','[':']'}
        for i in s:
            if not stack or i in D or stack[-1] not in D:
                stack.append(i)
            elif  stack[-1] in D and D[stack[-1]] != i:
                stack.append(i)
            else:
                stack.pop()
        return len(stack) == 0