class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import Counter
        C = Counter(nums)
        ans = []
        for i in sorted(C.keys()):
            ans.extend([i] * C[i])
        for i in range(len(nums)):
            nums[i] = ans[i]
        return nums