class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        temp = []
        for n,f in freq.items():
            temp.append([n,f])
        temp.sort(key= lambda a:-a[1])
        return [x[0] for x in temp[:k]]
