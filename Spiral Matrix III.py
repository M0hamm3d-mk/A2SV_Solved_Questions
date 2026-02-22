class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        spiral = [[rStart,cStart]]
        if rows * cols == 1:
            return spiral
            
        r,c = rStart,cStart
        direction = [[0,1],[1,0],[0,-1],[-1,0]] # right,down,left,up
        steps = 0
        d = 0
        while len(spiral) < rows * cols :
            if d % 2 == 0: # moving right or left by one more element 
                steps += 1
            for _ in range(steps):
                r += direction[d][0]
                c += direction[d][1]
                if 0 <= r < rows and 0 <= c < cols:
                    spiral.append([r,c])
                    if len(spiral) == rows*cols:
                        return spiral
            d = (d+1) % 4 # 
        return spiral
