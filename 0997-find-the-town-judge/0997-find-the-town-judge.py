class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n== 1:
            return 1
        outdegree = defaultdict(int)
        indegree = defaultdict(int)
        for a,b in trust:
            outdegree[a] += 1
            indegree[b] += 1
        for a,b in trust:
            if outdegree[a] == 0 and indegree[a] == n-1:
                return a
            if outdegree[b] == 0 and indegree[b] == n-1:
                return b
        return  -1
    