class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        mini = 0
        pre = 0
        for i in range(n):
            pre += nums[i]
            mini = min(mini,pre)
        return abs(mini)+1
            