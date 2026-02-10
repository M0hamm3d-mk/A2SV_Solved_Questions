class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def helper(num):
            new_num = 0
            while num > 0:
                new_num +=(( num % 10) ** 2)
                num //= 10
            return new_num
        while n > 1 and n not in seen:
            seen.add(n)
            n = helper(n)
            if n == 1:
                return True
        if n == 1:
            return True
        return False
            
