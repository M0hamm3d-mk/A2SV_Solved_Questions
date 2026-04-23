class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        graph = defaultdict(list)
        n = len(isConnected)
        for r in range(n):
            for c in range(n):
                if isConnected[r][c] and r != c:
                    graph[r].append(c)
                    graph[c].append(r)
        visited = [False] * n
        def dfs(node):
            visited[node]  = True
            for neighbour in graph[node]: 
                if not visited[neighbour]:
                    dfs(neighbour)
        for c in range(n):
            if not visited[c]:
                dfs(c)
                provinces += 1
        return provinces