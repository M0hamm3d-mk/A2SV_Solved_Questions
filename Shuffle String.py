class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        new_s = {}
        for i in range(n):
            new_s[indices[i]] = s[i]
        res = [0] * n
        for index,character in new_s.items():
            res[index] = character
        return "".join(res)
