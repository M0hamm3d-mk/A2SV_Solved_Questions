class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        max_dq = deque()  
        min_dq = deque()  
        left = 0
        res = 0

        for right in range(n):
            while max_dq and nums[right] > max_dq[-1]:
                max_dq.pop()
            max_dq.append(nums[right])

            while min_dq and nums[right] < min_dq[-1]:
                min_dq.pop()
            min_dq.append(nums[right])

            while max_dq[0] - min_dq[0] > limit:
                if nums[left] == max_dq[0]:
                    max_dq.popleft()
                if nums[left] == min_dq[0]:
                    min_dq.popleft()
                left += 1
            res = max(res, right - left + 1)

        return res