class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if  "" in strs:
            return ""
        res = []
        idx = 0
        if len(strs) == 1 and strs[0] != "":
            return strs[0]
        for i in strs[0]:
            res.append(i)
            for j in strs[1:]:
                if not j.startswith("".join(res)):
                    res.pop()
                    return "".join(res) if res else ""
        return "".join(res) if res else ""
    
                