class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def firstCivil(arr):
            low = 0
            high = len(arr) - 1

            while low <= high:
                mid = (low+high) // 2
                if arr[mid] == 0:
                    high = mid - 1
                else:
                    low  = mid + 1
            return low
            
        n = len(mat)
        m = len(mat[0])

        arr = []
        for i in range(n):
            arr.append([i,firstCivil(mat[i])])
        arr.sort(key=lambda a:(a[1]))

        return [x[0] for x in arr[:k]]
        