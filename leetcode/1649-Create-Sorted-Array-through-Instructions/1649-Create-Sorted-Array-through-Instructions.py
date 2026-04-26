class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        nums = []
        cost = 0

        for i in instructions:
            left = bisect.bisect_left(nums, i)
            right = bisect.bisect_right(nums, i)

            less = left
            greater = len(nums) - right

            cost = (cost + min(less, greater)) % MOD

            nums.insert(left,i)

        return cost