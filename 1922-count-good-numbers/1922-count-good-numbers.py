class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(x,n):
            if n == 0:
                return 1
            res = power(x,n//2)
            if n % 2:
                return x * res * res  % (10**9 + 7)
            return res * res % (10**9 + 7)
        
        
    
        p5 = power(5,math.ceil(n/2)) 
        p4 = power(4,n//2)
        return (p5 * p4) % (10**9 + 7)



        