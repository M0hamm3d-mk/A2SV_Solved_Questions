class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            res += (list(map(int,str(i))))
        return res
