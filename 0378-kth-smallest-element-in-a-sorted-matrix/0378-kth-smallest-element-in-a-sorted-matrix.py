class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                nums.append(matrix[i][j])
        return nsmallest(k,nums)[k-1]
            