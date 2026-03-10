class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        next_g = {}
        for n in nums2:
            while stack and stack[-1] < n:
                next_g[stack.pop()] = n
            stack.append(n)
        for n in nums1:
            if n not in next_g:
                res.append(-1) 
            else:
                res.append(next_g[n])
        return res
            