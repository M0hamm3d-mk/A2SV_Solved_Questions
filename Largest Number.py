class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        longest = 0
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            if len(nums[i]) > longest:
                longest = len(nums[i])
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                a = nums[j] * longest
                b = nums[j+1] * longest
                if a < b:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        return "".join(nums) if nums[0] != '0' else '0'
