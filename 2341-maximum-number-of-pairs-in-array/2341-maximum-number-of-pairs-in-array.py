class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        left = 0
        form = 0
        for num in cnt:
            if cnt[num] % 2:
                left += 1
            form += cnt[num] // 2
        return [form,left]