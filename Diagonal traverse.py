class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = [mat[0][0]]
        row = len(mat)
        col = len(mat[0])
        memo  = []
        if row == 1:
            return mat[0]
        for c in range(1,col):
            curr_c = c
            curr_r = 0
            temp = []
            while curr_c >= 0 and  0 <= curr_r < row:
                temp.append(mat[curr_r][curr_c])
                curr_r += 1
                curr_c -= 1
            memo.append(temp)
        for r in range(1,row):
            curr_r = r
            curr_c = col - 1
            temp = []
            while curr_r < row and 0 <= curr_c < col:
                temp.append(mat[curr_r][curr_c])
                curr_c -= 1
                curr_r += 1
            memo.append(temp)
        for i in range(len(memo)):
            if i % 2 == 0:
                res.extend(memo[i])
            else:
                res.extend(memo[i][::-1])
            i += 1
        return res

