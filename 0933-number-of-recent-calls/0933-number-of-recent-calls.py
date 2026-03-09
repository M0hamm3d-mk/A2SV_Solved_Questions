class RecentCounter:

    def __init__(self):
        self.deque = deque()
        self.index = 0
    def ping(self, t: int) -> int:
        self.deque.append(t)
        while self.deque and t - 3000 > self.deque[0]:
            self.deque.popleft()
        return len(self.deque) 
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)