class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row,col = len(img),len(img[0])
        smother = [[0 for _ in range(col)] for _ in range(row)]
        print(smother)
        for r in range(row):
            for c in range(col):
                valid = 1
                total = img[r][c]
                if r - 1 >= 0 and c-1 >= 0:
                    valid += 1
                    total += img[r-1][c-1]
                if r - 1 >= 0 and c >= 0:
                    valid += 1
                    total += img[r-1][c]
                if r - 1 >= 0 and c + 1 < col:
                    valid += 1
                    total += img[r-1][c+1]
                if r  >= 0 and c + 1 < col:
                    valid += 1
                    total += img[r][c+1]
                if r  >= 0 and c - 1 >= 0:
                    valid += 1
                    total += img[r][c-1]
                if r + 1 < row and c >= 0:
                    valid += 1
                    total += img[r+1][c]
                if r + 1 < row and c - 1 >= 0:
                    valid += 1
                    total += img[r+1][c-1]
                if r + 1 < row and c + 1 < col:
                    valid += 1
                    total += img[r+1][c+1]
                smother[r][c] = total//valid
        return smother

