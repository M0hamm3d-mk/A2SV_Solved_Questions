class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # lower bound
        low = 0
        high = len(nums) - 1
        flag = 0
        ans = []

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                if nums[mid] == target:
                    flag = 1
                high = mid - 1
            else:
                low = mid + 1

        if flag :
             ans.append(low)
        else:
            ans.append(-1)

        # upper bound
        low = 0
        high = len(nums) - 1
        flag = 0
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                if nums[mid] == target:
                    flag = 1
                    low = mid + 1
                else:
                    high = mid - 1
                    
            else:
                low = mid + 1

        if flag :
             ans.append(high)
        else:
            ans.append(-1)

        return ans