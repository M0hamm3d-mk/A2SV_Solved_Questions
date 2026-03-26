class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        size = len(nums)
        patches = 0
        curr = 1
        index = 0
        while curr <= n:
            if index < size and nums[index] <= curr :
                curr += nums[index]
                index += 1
            else:
                patches += 1
                curr += curr 
        return patches