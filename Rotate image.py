class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """  
        swapped = set() 
        rows = len(matrix)
        for r in range(rows):
            for c in range(rows):
                if (c,r) not in swapped and (r,c) not in swapped:
                    matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]
                    swapped.add((c,r))
                    swapped.add((r,c))
            matrix[r] = matrix[r][::-1]
                
                
