class Solution:
    def smallestNumber(self, pattern: str) -> str:
        used = [False] * 10
        res = []

        def backtrack(path):
            if len(path) == len(pattern) + 1:
                res.append("".join(path))
                return

            for num in range(1, 10):
                if used[num]:
                    continue
                if path:
                    i = len(path) - 1
                    if pattern[i] == 'I' and int(path[-1]) >= num:
                        continue
                    if pattern[i] == 'D' and int(path[-1]) <= num:
                        continue
                used[num] = True
                path.append(str(num))

                backtrack(path)

                path.pop()
                used[num] = False

        backtrack([])
        return min(res)