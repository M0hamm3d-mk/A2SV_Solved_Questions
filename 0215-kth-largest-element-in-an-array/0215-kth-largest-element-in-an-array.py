class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)

        k = n - k

        def quickSelect(l,r):
            pv,p = nums[r],l
            for i in range(l,r):
                if nums[i] < pv:
                    nums[p],nums[i] = nums[p],nums[i]
                    p += 1
            nums[p],nums[r] = nums[r],nums[p]

            if p > k :
                return quickSelect(l,p-1)
            elif p < k:
                return quickSelect(p+1,r)
            else:
                return nums[p]

        return quickSelect(0,n-1)
        