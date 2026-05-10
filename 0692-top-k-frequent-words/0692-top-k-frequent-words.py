class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        min_heap = []
        for word,frq in freq.items():

            heappush(min_heap,(-frq,word))
        ans = []
        for _ in range(k):
            ans.append(heappop(min_heap)[1])
        return ans