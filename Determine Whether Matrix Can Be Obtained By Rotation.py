class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            swapped = set() 
            rows = len(mat)
            for r in range(rows):
                for c in range(rows):
                    if (c,r) not in swapped and (r,c) not in swapped:
                        mat[r][c],mat[c][r] = mat[c][r],mat[r][c]
                        swapped.add((c,r))
                        swapped.add((r,c))
                mat[r] = mat[r][::-1]
            if mat == target:
                return True

        return False
