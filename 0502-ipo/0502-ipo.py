class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(capital)
        for i in range(n):
            capital[i] = (capital[i],profits[i])
        capital.sort()

        max_heap = []
        i = 0

        while k :
            while i < n and capital[i][0] <= w:
                heappush(max_heap,-capital[i][1])
                i += 1
            if max_heap:
                w += -heappop(max_heap)
            k -= 1
        
        return w
            



        