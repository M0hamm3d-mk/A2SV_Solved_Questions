class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        def check(mid):
            cnt = 0
            i = 0
            while i < n:
                i = bisect_left(position,position[i] + mid)
                cnt += 1
            return cnt >= m


        low = 1
        high = max(position) - position[0]
        res = 0
        while low <= high:
            mid = (low+high) // 2
            if check(mid):
                low = mid + 1
                res = max(res,mid)
            else:
                high = mid - 1
        return res
