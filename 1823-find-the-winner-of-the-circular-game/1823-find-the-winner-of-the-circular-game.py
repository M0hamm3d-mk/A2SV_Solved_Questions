class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [x for x in range(1,n+1)]
        def helper(players,k):
            m = len(players)
            if m == 1:
                return players[0]
            size = m * k + 2
            for i in range(size):
                if i % size == k - 1:
                    players = players[(k - 1)%m + 1:] + players[:(k-1)%m]
                    return helper(players,k)
                        
        return helper(nums,k)
        