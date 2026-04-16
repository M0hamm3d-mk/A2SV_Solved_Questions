class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        fast = slow = nums[i]
        while i < len(nums):
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                break
            i += 1
        i = 0
        fast = nums[i]

        while i < len(nums):
            fast = nums[fast]
            if fast == slow:
                return slow
            i += 1