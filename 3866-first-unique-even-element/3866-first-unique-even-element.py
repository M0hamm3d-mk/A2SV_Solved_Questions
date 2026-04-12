class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        cnter = Counter(nums)
        for i in nums:
            if not i % 2 and cnter[i] == 1:
                return i
        return -1