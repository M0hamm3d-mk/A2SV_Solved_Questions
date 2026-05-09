class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)

        min_heap = []

        for i in range(min(k,n)):
            heappush(min_heap,(nums1[i] + nums2[0],i,0))

        ans = []
        while min_heap and len(ans) < k:
            comb,r,c = heappop(min_heap)
            ans.append([nums1[r],nums2[c]])
            if c + 1 < m:
                heappush(min_heap,(nums1[r] + nums2[c+1],r,c+1))
        return ans
            
