class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        low = 0
        high = num // 2
        while low <= high:
            mid = (low+high) // 2
            # print(mid)
            if mid * mid == num:
                return True
            if mid * mid > num:
                high = mid - 1
            else:
                low = mid + 1
        return False