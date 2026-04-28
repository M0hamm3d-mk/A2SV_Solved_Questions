class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])

        dn = [(0,1),(0,-1),(1,0),(-1,0)]

        def inbound(row,col):
            return 0 <= row < n and 0 <= col < m
        visited = [[False for _ in range(m)] for _ in range(n)]
        cycle = False

        def dfs(r,c,pr,pc):
            # print("here")
            nonlocal cycle
            if cycle:
                return 
            visited[r][c]  = True
            # print('here')
            for dr,dc in dn:
                nr = r + dr
                nc = c + dc
         
                print(nr, nc)
                if inbound(nr,nc) and  grid[nr][nc] == grid[r][c]:
                    if not visited[nr][nc]:
                        # visited[nr][nc] = True
                        dfs(nr,nc,r,c)

                    elif pr != nr or pc != nc:
                        cycle = True
        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    # print('here')
                    dfs(i,j,-1,-1)

        return cycle
