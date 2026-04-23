class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        graph = defaultdict(list)
        n = len(isConnected)
        visited = [False] * n
        def dfs(i):
            visited[i]  = True
            for j in range(n): 
                if not visited[j] and isConnected[i][j]:
                    dfs(j)
        for c in range(n):
            if not visited[c]:
                dfs(c)
                provinces += 1
        return provinces