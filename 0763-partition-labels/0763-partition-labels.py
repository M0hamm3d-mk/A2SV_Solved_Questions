class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        last_index = {}
        for i,v in enumerate(s):
            last_index[v] = i
        res = []
        i = 0
        while i < n:
            j = i
            length = last_index[s[i]] - i + 1
            
            while j < max(last_index[s[i]],length):
                length = max(length,last_index[s[j]] - i + 1)
                j += 1
            res.append(length)
            i += length
        return res