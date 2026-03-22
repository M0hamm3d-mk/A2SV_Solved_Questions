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
                    # if the last player is gonna be elliminated
                    if (k-1) % m == m - 1:
                       players.pop()
                       return helper(players,k)

                    # if the first player is gonna be elliminated
                    elif (k-1) % m == 0:
                       return helper(players[1:],k)

                    # any player in the middle is gonna be elliminated
                    else:
                        return helper(players[k % m:] + players[:(k-1)%m],k)
                        
        return helper(nums,k)
        