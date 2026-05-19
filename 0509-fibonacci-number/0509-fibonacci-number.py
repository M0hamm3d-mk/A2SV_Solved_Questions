class Solution:
    def fib(self, n: int) -> int:
        memo = {0:0,1:1}
        def dp(num,memo):
            if num in memo:
                return memo[num]
            memo[num] = dp(num-1,memo) + dp(num-2,memo)
            return memo[num]
        return dp(n,memo)
        