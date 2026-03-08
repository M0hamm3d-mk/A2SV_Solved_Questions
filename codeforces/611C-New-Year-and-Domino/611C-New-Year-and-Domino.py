def newYear():
    row,col = map(int,input().split())
    grid = [input().strip() for _ in range(row)]
    horizontal_domino = [[0]*col for _ in range(row)]
    vertical_domino = [[0]*col for _ in range(row)]
    
    # mark horizontal dominos
    for r in range(row):
        for c in range(col-1):
            if grid[r][c] == '.' == grid[r][c+1]:
                horizontal_domino[r][c] = 1
               
                
    # mark vertical dominos
    for r in range(row-1):
        for c in range(col):
            if grid[r][c] == '.' == grid[r+1][c]:
                vertical_domino[r][c] = 1
                
    pre_h = [[0] * (col + 1) for _ in range(row+1)] 
    pre_v = [[0] * (col + 1) for _ in range(row+1)] 
    
    # prefix sum for horizontal domino
    for i in range(row):
        for j in range(col):
            pre_h[i+1][j+1] = horizontal_domino[i][j] + pre_h[i][j+1] + pre_h[i+1][j] - pre_h[i][j]
            
            
    # prefix sum for vertical domino
    for i in range(row):
        for j in range(col):
            pre_v[i+1][j+1] = pre_v[i][j+1] + pre_v[i+1][j] + vertical_domino[i][j] - pre_v[i][j]
    
    
    q = int(input())
    for _ in range(q):
        r1,c1,r2,c2 = map(int,input().split())

        h = pre_h[r2][c2-1] - pre_h[r1-1][c2-1] - pre_h[r2][c1-1] + pre_h[r1-1][c1-1]
        v = pre_v[r2-1][c2] - pre_v[r1-1][c2] - pre_v[r2-1][c1-1] + pre_v[r1-1][c1-1]

        print(h+v)
        
newYear()