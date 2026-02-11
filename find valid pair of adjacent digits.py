class Solution:
    def findValidPair(self, s: str) -> str:
        freq = Counter(s)
        i = 0
        n = len(s)
        while i < n-1:
            if freq[s[i]] == int(s[i]) and freq[s[i+1]] == int(s[i+1]) and s[i] != s[i+1]:
                return "".join([s[i],s[i+1]])
            i += 1
        return ''

