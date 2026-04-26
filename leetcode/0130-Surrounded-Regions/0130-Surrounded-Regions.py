class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = len(board)
        m = len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def inbound(r,c):
            return 0 <= r < n and 0 <= c < m

        def dfs(row,col):
            stack = [(row,col)]
            while stack:
                r,c = stack.pop()
           
                for i,j in directions:
                    nr = r + i
                    nc =  c + j

                    if inbound(nr,nc) and board[nr][nc] == 'O':
                        board[nr][nc] = 'N'
                        stack.append((nr,nc))


        for c in range(m):
            if board[0][c] == 'O':
                board[0][c] = 'N'
                dfs(0,c)
            if board[n-1][c] == 'O':
                board[n-1][c] = 'N'
                dfs(n-1,c)
        for r in range(n):
            if board[r][0] == 'O':
                board[r][0] = 'N'
                dfs(r,0)
            if board[r][m-1] == 'O':
                board[r][m-1] = 'N'
                dfs(r,m-1)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'N':
                    board[i][j] = 'O'