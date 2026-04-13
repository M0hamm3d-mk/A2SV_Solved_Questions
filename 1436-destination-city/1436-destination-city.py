class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = set([x[0] for x in paths])
        for p in paths:
            if p[1] not in d:
                return p[1]
