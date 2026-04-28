class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def inbound(row,col):
            return 0 <= row < n and 0 <= col < m
        visited = [[False for _ in range(m)] for _ in range(n)]
        def dfs(r,c,pr,pc):
            visited[r][c] = True
            for dr,dc in directions:
                nr,nc = r + dr , c + dc
                # if not inbound(nr,nc): continue
                # elif grid[nr][nc] != grid[r][c]: continue
                if inbound(nr,nc) and grid[nr][nc] == grid[r][c]:
                    if not visited[nr][nc]:
                        if dfs(nr,nc,r,c):
                            return True

                    elif (nr,nc) != (pr,pc):
                        return True
        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    if dfs(i,j,-1,-1):
                        return True
        return False