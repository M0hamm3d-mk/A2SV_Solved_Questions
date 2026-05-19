class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {0:0,1:1,2:2}
        def ways(step):
            if step in dp:
                return dp[step]
            dp[step] = ways(step-1) + ways(step-2)
            return dp[step]
        return ways(n)
            