class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left,right = 0, int(c ** (1/2))
        while left <= right:
            s = left ** 2 + right ** 2
            if s < c:
                left += 1
            elif s > c:
                right -= 1
            else:
                return True
        return False