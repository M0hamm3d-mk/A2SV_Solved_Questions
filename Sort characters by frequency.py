class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        s = list(s)
        s.sort(key=lambda a: (-freq[a],a))
        return "".join(s)
