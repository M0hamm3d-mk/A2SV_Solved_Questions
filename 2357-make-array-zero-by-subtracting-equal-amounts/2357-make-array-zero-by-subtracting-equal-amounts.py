class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        op = 0
        while max(nums) > 0 and nums:
            sub = 0
            heapify(nums)
            while nums[0] == 0:
                heappop(nums)
            sub = nums[0]

            for i in range(len(nums)):
                nums[i] -= sub
            op += 1
        return op