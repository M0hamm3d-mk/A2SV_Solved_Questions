class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float('inf')
        def devide(arr):
            n = len(arr)
            if n <= 1:
                return arr[0]
            mid = n // 2
            left = arr[:mid]
            right = arr[mid:]

            return min(devide(left),devide(right),ans)
        return devide(nums)