class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n  for _ in range(n)]
        colSet = set()
        decDiag = set()
        incDiag = set()
        def backTrack(row):
            if row == n :
                res.append(["".join(r) for r in board[:]])
                return
            for col in range(n):
                if col not in colSet and  row - col not in decDiag and row + col not in incDiag:
                    colSet.add(col)
                    decDiag.add(row-col)
                    incDiag.add(row+col)
                    board[row][col] = 'Q'

                    backTrack(row+1)

                    colSet.remove(col)
                    decDiag.remove(row-col)
                    incDiag.remove(row+col)
                    board[row][col] = '.'
        backTrack(0)

        return res