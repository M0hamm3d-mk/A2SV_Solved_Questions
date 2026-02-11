class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = Counter(nums)
        dominant = nums[0]
        for i in nums:
            if freq[i] > freq[dominant]:
                dominant = i
        freq_d = freq[dominant]
        d = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == dominant:
                d += 1
            if d > (i+1) //2  and  freq_d-d > (n-i-1) // 2:
                return i
        return -1
            
