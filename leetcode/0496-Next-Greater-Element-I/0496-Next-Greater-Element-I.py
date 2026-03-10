class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
    
        for i in nums1:
            temp = nums2.copy()
            nearest_large = i

            while temp[-1] != i:
                if temp[-1] > i:
                    nearest_large = temp[-1]
                temp.pop()

            if nearest_large == i:
                res.append(-1)
            else:
                res.append(nearest_large)
                
        return res


# optimal solution
# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         res = []
#         stack = []
#         next_g = {}
#         for n in nums2:
#             while stack and stack[-1] < n:
#                 next_g[stack.pop()] = n
#             stack.append(n)
#         for n in nums1:
#             if n not in next_g:
#                 res.append(-1) 
#             else:
#                 res.append(next_g[n])
#         return res
