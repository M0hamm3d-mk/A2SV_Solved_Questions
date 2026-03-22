class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [x for x in range(1,n+1)]
        def ellinator(players,k):
            if len(players) == 1:
                return players[0]
            size = len(players) * k + 2
            for i in range(size):
               if i % size == k - 1:
                    if (k-1) % len(players) == len(players) - 1:
                       players.pop()
                       return ellinator(players,k)
                    elif (k-1) % len(players) == 0:
                       return ellinator(players[1:],k)
                    else:
                        return ellinator(players[k % len(players):] + players[:(k-1)%len(players)],k)
        return ellinator(nums,k)
        