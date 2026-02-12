class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_r,freq_m = Counter(ransomNote),Counter(magazine)
        for k in freq_r:
            if freq_r[k] > freq_m[k]:
                return False
        return True
