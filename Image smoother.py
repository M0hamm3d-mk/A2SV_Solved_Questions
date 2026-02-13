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


# optional and clean way

# class Solution:
#     def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
#         row,col = len(img),len(img[0])
#         smother = [[0 for _ in range(col)] for _ in range(row)]
#         for r in range(row):
#             for c in range(col):
#                 valid = 0
#                 total = 0
#                 for i in range(-1,2):
#                     for j in range(-1,2):
#                         curr_r = r + i
#                         curr_c = c + j
#                         if 0 <= curr_r < row and 0 <= curr_c < col:
#                             total += img[curr_r][curr_c]
#                             valid += 1
#                 smother[r][c] = total//valid
#         return smother


