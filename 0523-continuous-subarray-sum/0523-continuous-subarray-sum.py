class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        pre = 0
        memo = {0:-1}
        print(0%1)
        for i in range(n):
            pre += nums[i]

            if pre % k in memo and i - memo[pre%k] + 1 > 2:
                return True
            if pre % k not in memo:
                memo[pre % k] = i

        return False