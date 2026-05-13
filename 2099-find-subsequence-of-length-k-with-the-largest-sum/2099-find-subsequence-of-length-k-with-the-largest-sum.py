class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        for i in range(len(nums)):
            heappush(min_heap,(nums[i],i))
        
        for _ in range(len(nums)-k):
            heappop(min_heap)
        min_heap.sort(key=lambda a: a[1])
        return [x[0] for x in min_heap]
        