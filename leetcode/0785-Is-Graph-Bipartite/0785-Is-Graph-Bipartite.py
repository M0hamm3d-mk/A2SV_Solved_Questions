class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        m = len(graph[0])
        color = [-1] * n
        visited = [False] * n
        paint = {1:0,0:1}
        def dfs(node,group):
            visited[node] = True
            if color[node] == -1:
                color[node] = group
            elif color[node] != group:
                return False
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    if not dfs(neighbour,paint[group]):
                        return False
                else:
                    if color[neighbour] != paint[group]:
                        return False
            return True
        for i in range(n):
            if not visited[i]:
                if not dfs(i, 0):
                    return False
        return True