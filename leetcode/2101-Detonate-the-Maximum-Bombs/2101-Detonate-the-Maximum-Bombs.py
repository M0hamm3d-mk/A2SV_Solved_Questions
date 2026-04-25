class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # bombs.sort()

        graph = defaultdict(list)
        n = len(bombs)
        for i in range(n):
            curr_x = bombs[i][0]
            curr_y = bombs[i][1]
            curr_r = bombs[i][2]
            for j in range(n):
                if i != j:
                    x = bombs[j][0]
                    y = bombs[j][1]
                    r = bombs[j][2]
                    if ((curr_x - x) ** 2 + (curr_y - y) ** 2) <= (curr_r) ** 2:
                        graph[i].append(j)
                
        res = 0
        for i in range(n):
                visited = set([i])
                stack = [i]
                t = 0
                while stack:
                    node = stack.pop()
                    t += 1
                    for neighbour in graph[node]:
                        if not neighbour in visited:
                            visited.add(neighbour)
                            stack.append(neighbour)
                res = max(res,t)
        return res