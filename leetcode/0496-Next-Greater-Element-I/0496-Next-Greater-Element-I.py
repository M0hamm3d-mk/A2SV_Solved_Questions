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