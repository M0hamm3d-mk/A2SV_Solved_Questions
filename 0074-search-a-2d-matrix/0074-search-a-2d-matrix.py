class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row
        low = 0
        high = len(matrix) - 1
        r = -1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][-1] >= target:
                high = mid - 1
                r = mid
            else:
                low = mid + 1
        print(r)
        # find the target in the row
        if r == -1:
            return False
        row = matrix[r]
        low = 0
        high = len(row) - 1
        while low <= high:
            mid = (low + high) // 2
            if row[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return row[low] == target 
        

