class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = [value]
        self.kk = k
        self.vv = value
        self.cnt = 0
    def consec(self, num: int) -> bool:
        self.stream.append(num)
        if num == self.vv and self.cnt + 1 >= self.kk:
            self.cnt += 1
            return True
        if num != self.vv:
            self.cnt = 0
            return False
        if num == self.vv:
            self.cnt += 1
            return False
     
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)