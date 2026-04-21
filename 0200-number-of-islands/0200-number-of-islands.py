class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = [[False for _ in range(m)] for _ in range(n)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        island = 0

        def inbound(row,col):
            return (0 <= row < n) and (0 <= col < m)

        def dfs(row,col):
            nonlocal island

            for r,c in directions:
                new_row = row + r
                new_col = col + c

                if inbound(new_row,new_col) and not visited[new_row][new_col] and grid[new_row][new_col] == '1':
                    visited[new_row][new_col] = True
                    dfs(new_row,new_col)
        for row in range(n):
            for col in range(m):
                if grid[row][col] == '1' and not visited[row][col]:
                    visited[row][col] = True
                    dfs(row,col)
                    island += 1
        return island
        
        
        