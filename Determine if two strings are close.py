class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        v1 = [x for x in freq1.values()]
        v2 = [x for x in freq2.values()]
        for i in freq1:
            if i not in freq2:
                return False
        return sorted(v1) == sorted(v2)
