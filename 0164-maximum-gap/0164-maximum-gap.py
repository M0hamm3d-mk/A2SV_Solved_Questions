class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        def bucket_sort(arr, n):
            mx,mn = max(arr),min(arr)
            rn = mx - mn 
            if rn == 0:
                return arr
            bucket = [[] for _ in range(n)]
            for i in range(n):
                idx = int((arr[i] - mn )/rn * (n-1))
                bucket[idx].append(arr[i])
            res = []
            for b in bucket:
                res.extend(sorted(b))
            return res
        if len(nums) < 2:
            return 0
        new_arr = bucket_sort(nums,len(nums))
        res = 0 
        l,r = 0,1
        while r < len(new_arr):
            res = max(res,new_arr[r]-new_arr[l])
            l += 1
            r += 1
        return res

