class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)
        low = 1
        high =max(candies)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            childs = sum(c//mid for c in candies)
            if childs >= k:
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
        return ans