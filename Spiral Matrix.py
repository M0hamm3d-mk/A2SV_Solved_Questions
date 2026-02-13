class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = 0 
        c = 0
        row = len(matrix)
        col = len(matrix[0])
        res = []
        traversed = set()
        direction = 'R' # \'R','D','L','U'\ right,down,left,up
        top_boarder = -1
        right_boarder = col
        bottom_boarder = row
        left_boarder = -1
        while True:
            if direction == 'R':
                while  c < right_boarder :
                    res.append(matrix[r][c])
                    c += 1
                c -= 1
                r += 1
                top_boarder += 1
                if top_boarder == bottom_boarder or len(res) == row * col:
                    return res 
                direction = 'D'
            elif direction == 'D':
                while top_boarder < r < bottom_boarder:
                    res.append(matrix[r][c])
                    r += 1
                r -= 1
                c -= 1
                right_boarder -= 1
                if right_boarder == left_boarder or len(res) == row * col:
                    return res
                direction = 'L'
            elif direction == 'L':
                while c > left_boarder:
                    res.append(matrix[r][c])
                    c -= 1
                c += 1
                r -= 1
                bottom_boarder -= 1
                if bottom_boarder == top_boarder or len(res) == row * col:
                    return res 
                direction = 'U'
            else:
                while r > top_boarder:
                    res.append(matrix[r][c])
                    r -= 1
                left_boarder += 1
                r += 1
                c += 1
                if left_boarder == right_boarder or len(res) == row * col:
                    return res 
                direction = 'R'
            
