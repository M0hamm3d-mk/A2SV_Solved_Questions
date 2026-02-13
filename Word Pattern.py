class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        maps = {}
        mapsR = {}
        for i in range(len(pattern)) :
            if pattern[i] in maps and maps[pattern[i]] != s[i]:
                return False
            if s[i] in mapsR and mapsR[s[i]] != pattern[i]:
                return False
            maps[pattern[i]] = s[i]
            mapsR[s[i]] = pattern[i]
        return True 
