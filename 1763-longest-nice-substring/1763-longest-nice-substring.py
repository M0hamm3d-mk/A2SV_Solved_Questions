class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) == 1:
            return ''
        for i in range(len(s)):
            if s[i].swapcase() not in set(s):
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return max(left,right ,key=len)
        return s