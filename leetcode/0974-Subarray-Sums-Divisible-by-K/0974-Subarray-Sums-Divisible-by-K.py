class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        memo = {0:1}
        pre = 0
        res = 0
        for i in range(len(nums)):
            pre += nums[i]
            if pre % k in memo:
                res += memo[pre % k]
            memo[pre % k] = memo.get(pre % k,0)+1
        return res