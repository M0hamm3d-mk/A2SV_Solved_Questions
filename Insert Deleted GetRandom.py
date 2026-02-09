import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.indexes = {}

    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False
        n = len(self.arr)
        self.indexes[val] = n
        self.arr.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.indexes:
            return False
        last = self.arr[-1]
        delete = self.indexes[val]
        self.arr[delete] = last
        self.indexes[last] = self.indexes[val]
        self.arr.pop()
        del self.indexes[val]
        return True
    def getRandom(self) -> int:
        return random.choice(self.arr)


        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
