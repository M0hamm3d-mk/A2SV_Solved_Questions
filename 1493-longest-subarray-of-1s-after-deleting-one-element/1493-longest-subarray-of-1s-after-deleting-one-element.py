class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        left = 0
        _sum = 0
        for right in range(n):
            _sum += nums[right]
            while right - left + 1 - _sum > 1:
                _sum -= nums[left]
                left += 1
            res = max(res,right - left )
        return res
