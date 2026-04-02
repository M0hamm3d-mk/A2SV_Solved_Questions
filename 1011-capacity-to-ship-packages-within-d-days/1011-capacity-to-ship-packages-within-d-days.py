class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        def helper(max_cap):
            days_needed = 0
            running_sum = 0
            # limit = 0
            for w in weights:

                if running_sum + w > max_cap:
                    running_sum = 0
                    days_needed += 1
                running_sum += w
           
            return days_needed + 1
     
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            day = helper(mid)
            if day <= days:
                high  = mid - 1
            else:
                low = mid + 1
        return low
