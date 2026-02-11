class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        freq = Counter(changed) 
        ans = []
        zero = freq[0]
        if zero % 2 != 0:
            return []
        if len(changed) % 2 != 0:
            return []
        changed.sort()
        for i in changed:
            if i in freq:
                if i * 2 in freq:
                    ans.append(i)
                    freq[i*2] -= 1
                    freq[i] -= 1
                    if freq[i*2] == 0:
                        del freq[i*2]
                    if freq[i] == 0:
                        del freq[i]
        
        return ans if len(ans) == len(changed)//2 else []
