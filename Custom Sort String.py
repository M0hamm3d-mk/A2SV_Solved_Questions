class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        _set = set(order)
        res = []
        for i in order:
            res.append(i*freq[i])
        for i in s:
            if i not in _set:
                res.append(i)
        return "".join(res)
