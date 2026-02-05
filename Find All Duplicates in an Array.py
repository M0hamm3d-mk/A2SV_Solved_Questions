class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        freq = Counter(nums)
        for i in freq:
            if freq[i] == 2:
                res.append(i)
        return res
