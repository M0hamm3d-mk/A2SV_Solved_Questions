class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        D = defaultdict(int)
        n = len(nums)//3
        ans = []
        for i in nums:
            D[i] += 1
        for i in D:
            if D[i] > n:
                ans.append(i)
        return ans
