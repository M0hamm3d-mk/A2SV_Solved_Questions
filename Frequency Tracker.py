class FrequencyTracker:

    def __init__(self):
        self.numbers = {}
        self.freq = {}

    def add(self, number: int) -> None:
        self.deleted = self.numbers.get(number,0)
        if self.deleted in self.freq:
            self.freq[self.deleted] -= 1
            if self.freq[self.deleted] == 0:
                del self.freq[self.deleted]

        self.numbers[number] = self.numbers.get(number,0)+1
        self.freq[self.numbers[number]] = self.freq.get(self.numbers[number],0) + 1
    def deleteOne(self, number: int) -> None:
        if number in self.numbers:
            self.freq[self.numbers[number]] -= 1
            if self.freq[self.numbers[number]] == 0:
                del self.freq[self.numbers[number]]
                
            self.numbers[number] -= 1
            if self.numbers[number] != 0:
                self.freq[self.numbers[number]] = self.freq.get(self.numbers[number],0) + 1
            else:
                del self.numbers[number]

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
