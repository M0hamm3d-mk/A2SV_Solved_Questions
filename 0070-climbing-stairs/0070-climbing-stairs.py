class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {0:0,1:1,2:2}
        def ways(step,dp):
            if step in dp:
                return dp[step]
            dp[step] = ways(step-1,dp) + ways(step-2,dp)
            return dp[step]
        return ways(n,dp)
            