class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        ans = 0

        for h in houses:
            i = bisect_left(heaters,h)

            left = right =float('inf')
            if i < len(heaters):
                right = heaters[i] - h
            if i > 0:
                left = h - heaters[i-1]

            ans = max(ans,min(right,left))
        return ans
            