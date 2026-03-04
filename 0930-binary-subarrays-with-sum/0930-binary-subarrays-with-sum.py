class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        memo = {0:1}
        res = 0
        pre = 0
        for i in range(n):
            pre += nums[i]
            if pre - goal in memo:
                res += memo[pre-goal]
            memo[pre] = memo.get(pre,0) + 1
        return res