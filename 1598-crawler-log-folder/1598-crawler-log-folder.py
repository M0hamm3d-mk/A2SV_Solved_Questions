class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack  = []
        for i in logs:
            if not stack and i != '../' and i != './':
                stack.append(i)
            elif i == '../':
                if stack:
                    stack.pop()
            elif i != './':
                stack.append(i)
        return len(stack)