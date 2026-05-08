class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        nums = []
        for i in range(n):
            heappush(nums,(matrix[i][0],i,0))
        for _ in range(k-1):
            v,r,c = heappop(nums)
            if c + 1 < n:
                heappush(nums,(matrix[r][c+1],r,c+1))
        return heappop(nums)[0]

            