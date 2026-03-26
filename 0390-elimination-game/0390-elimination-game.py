class Solution:
    def __init__(self,):
        self.step = 1
        self.turn = 'left'
        self.front = 1
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return self.front
        if self.turn == 'left' or n % 2:
            self.front += self.step
        self.step *= 2
        n //= 2
        if self.turn == 'left':
            self.turn = 'right'
        else:
            self.turn = 'left'
        return self.lastRemaining(n)

        