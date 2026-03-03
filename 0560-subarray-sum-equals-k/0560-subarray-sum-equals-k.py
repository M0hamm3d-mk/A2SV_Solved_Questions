class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = 0
        memo = {0:1} 
        res = 0

        for i in range(n):
            pre += nums[i]
            if pre - k in memo:
                res += memo[pre-k]
            memo[pre] = memo.get(pre,0) + 1

        return res