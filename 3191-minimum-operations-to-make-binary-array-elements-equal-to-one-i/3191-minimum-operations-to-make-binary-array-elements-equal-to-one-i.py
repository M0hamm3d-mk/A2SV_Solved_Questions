class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        op = 0
        for i in range(n-2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] = 1 - nums[i+1]
                nums[i + 2] = 1 - nums[i+2]
                op += 1
        return op if 0 not in set(nums) else -1