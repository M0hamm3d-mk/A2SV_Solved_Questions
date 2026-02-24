class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        i = 0

        while i < n :
            curr = haystack[i:i+m]
            if curr == needle:
                return i
            i += 1

        return -1