class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        arr = [-x for x in stones]
        heapq.heapify(arr)

        while arr:

            if len(arr) == 1:
                return -arr[0]
            a,b = -heapq.heappop(arr),-heapq.heappop(arr)

            if a != b:

                heapq.heappush(arr,-(a-b))
            heapq.heapify(arr)

        return 0