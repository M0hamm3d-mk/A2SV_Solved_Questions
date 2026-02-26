class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = Counter('')
        left = res = m = 0
        for right in range(n):
            freq[s[right]] += 1
            m = max(m,freq[s[right]])
            while right - left + 1 - m > k:
                freq[s[left]] -= 1
                left += 1
            res = max(res,right-left+1)
        return res