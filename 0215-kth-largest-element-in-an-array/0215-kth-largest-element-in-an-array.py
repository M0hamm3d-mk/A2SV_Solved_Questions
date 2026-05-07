class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_ = [-1 * x for x in nums]
        heapq.heapify(nums_)
        while k > 1:
            heapq.heappop(nums_)
            k -= 1
        return -1 * heapq.heappop(nums_)