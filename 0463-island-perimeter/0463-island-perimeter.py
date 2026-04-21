class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def inbound(row,col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))

        def dfs(row,col):
            nonlocal perimeter
            visited[row][col] = True
            for r,c in directions:
                new_row = row + r
                new_col = col + c
                if not inbound(new_row,new_col) or not grid[new_row][new_col]:
                    perimeter += 1
                elif grid[new_row][new_col] == 1 and not visited[new_row][new_col]:
                        dfs(new_row,new_col)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(row,col)
                    return perimeter
