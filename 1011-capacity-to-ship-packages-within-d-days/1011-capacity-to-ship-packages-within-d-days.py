class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        def helper(max_cap):
            days_needed = 0
            running_sum = 0
            limit = 0
            for w in weights:

                if running_sum + w < max_cap:
                    running_sum += w
                else:
                    limit = max(limit,running_sum)
                    running_sum = w
                    days_needed += 1
            if running_sum:
                days_needed += 1
            return [days_needed,limit]
     
        low = max(weights)
        high = sum(weights)
        if days == n:
            return low
        if days == 1:
            return high
        ans = high
        while low <= high:
            mid = (low + high) // 2
            day,limit = helper(mid)
            # print(low,mid,high,day)
            if day <= days:
                ans = min(ans,limit)   
                high  = mid - 1
            else:
                low = mid + 1
        return ans
