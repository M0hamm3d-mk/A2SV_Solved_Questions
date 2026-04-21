class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        island = 0

        def inbound(row,col):
            return (0 <= row < n) and (0 <= col < m)

        def dfs(row,col):
            nonlocal island
            grid[row][col] = '0'

            for r,c in directions:
                new_row = row + r
                new_col = col + c
                if inbound(new_row,new_col)  and grid[new_row][new_col] == '1':
                    dfs(new_row,new_col)
                    
        for row in range(n):
            for col in range(m):
                if grid[row][col] == '1':
                    dfs(row,col)
                    island += 1
        return island
        
        
        