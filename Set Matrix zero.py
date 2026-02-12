class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # mark the rows and columns that are gonna be zero
        zeros_row = set()
        zeros_col = set()
        row = len(matrix)
        col = len(matrix[0])
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    zeros_row.add(r)
                    zeros_col.add(c)
        for r in range(row):
            for c in range(col):
                if r in zeros_row or c in zeros_col:
                    matrix[r][c] = 0

        return matrix
