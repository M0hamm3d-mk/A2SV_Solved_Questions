class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            if row[-1] < 0:
                for j in row:
                    if j < 0:
                        count += 1
        return count
