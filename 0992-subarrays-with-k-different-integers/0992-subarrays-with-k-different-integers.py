class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(nums,k) :
            freq = Counter([])
            left = 0
            res = 0
            n = len(nums)
            for right in range(n):
                freq[nums[right]] += 1
                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1
                res += right - left + 1
            return res
        return helper(nums,k) - helper(nums,k-1)