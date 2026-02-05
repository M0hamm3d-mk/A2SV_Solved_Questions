class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq_chars = Counter(chars)
        total = 0
        for i in words:
            freq_i = Counter(i)
            yes = True
            for j in i:
                if freq_i[j] > freq_chars[j]:
                    yes = False
            if yes:
                total += len(i)
        return total
