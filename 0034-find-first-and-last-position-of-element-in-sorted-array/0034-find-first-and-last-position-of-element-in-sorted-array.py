class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # lower bound
        low = 0
        high = len(nums) - 1
        ans = []

        while low <= high:

            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1

        if low < len(nums) and nums[low] == target :
             ans.append(low)
        else:
            ans.append(-1)

        # upper bound
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                if nums[mid] == target:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                low = mid + 1

        if ans[0] != -1 :
             ans.append(high)
        else:
            ans.append(-1)

        return ans