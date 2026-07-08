class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ss = s1.split() + s2.split()
        ans = []
        sss = Counter(ss)
        for s in sss:
            if sss[s] == 1:
                ans.append(s)
        return ans