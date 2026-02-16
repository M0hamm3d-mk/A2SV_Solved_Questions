class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        _set = set(nums)
        seen = set()
        longest = 1
        for i in _set:
            if i - 1 not in _set:
                cons = 0
                while i in _set:
                    i += 1
                    cons += 1
                longest = max(longest,cons)
                cons = 0
        return longest
