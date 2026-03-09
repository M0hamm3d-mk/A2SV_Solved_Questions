class RecentCounter:

    def __init__(self):
        self.stack = []
        self.index = 0
    def ping(self, t: int) -> int:
        self.stack.append(t)
        if t - 3000 > self.stack[self.index]:
            self.index += 1
        return len(self.stack) - self.index
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)