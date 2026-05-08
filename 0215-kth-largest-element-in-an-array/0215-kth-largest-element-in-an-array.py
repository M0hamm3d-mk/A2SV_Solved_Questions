class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_ = [-x for x in nums]
        heapify(nums_)
        while k > 1:
            heappop(nums_)
            k -= 1
        return -nums_[0]