class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [x for x in range(1,n+1)]
        def helper(players,k):
            m = len(players)
            if m == 1:
                return players[0]
            for i in range(m):
                players = players[(k - 1)%m + 1:] + players[:(k-1)%m]
                return helper(players,k)
                        
        return helper(nums,k)
        