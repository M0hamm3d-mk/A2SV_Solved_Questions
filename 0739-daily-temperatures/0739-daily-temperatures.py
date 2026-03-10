class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        n = len(temperatures)
        stack = []
        next_g = {}
        for i in range(n):
            while stack and stack[-1][1] < temperatures[i]:
                popped = stack.pop()
                next_g[popped] = i - popped[0]
            stack.append((i,temperatures[i]))
        for i,t in enumerate(temperatures):
            if (i,t) not in next_g:
                res.append(0)
            else:
                res.append(next_g[(i,t)])
        return res