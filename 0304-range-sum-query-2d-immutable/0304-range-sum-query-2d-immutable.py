class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.pre = [[0 for _ in range(col+1)] for _ in range(row+1)]
        for r in range(row):
            for c in range(col):
                self.pre[r][c] = self.pre[r-1][c] + self.pre[r][c-1] - self.pre[r-1][c-1] + matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        upper = self.pre[row1-1][col2]
        left = self.pre[row2][col1-1]
        full = self.pre[row2][col2]
        overlap = self.pre[row1-1][col1-1]
        return full - upper - left + overlap
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)