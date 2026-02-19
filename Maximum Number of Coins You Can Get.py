class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        left = 0
        right = len(piles)-1
        while left < right:
            res += piles[right-1]
            right -= 2
            left += 1
        return res
