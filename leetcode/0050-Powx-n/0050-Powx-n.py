class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n *= -1
        if n == 0:
            return 1
        temp = self.myPow(x,n//2)
        if n % 2:
            return x * temp * temp
        return temp*temp