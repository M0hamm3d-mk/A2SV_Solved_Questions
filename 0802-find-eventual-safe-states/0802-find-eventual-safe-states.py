class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outdegree = [0] * n
        revgraph = defaultdict(list)
        for i in range(n):
            outdegree[i] = len(graph[i])
            for j in graph[i]:
                revgraph[j].append(i)
        
        q = deque()
        safe = [False] * n
        for i in range(n):
            if outdegree[i] == 0:
                q.append(i)

        # print(q)

        while q:
            course = q.popleft()
            safe[course] = True
            for c in revgraph[course]:
                outdegree[c] -= 1
                if outdegree[c] == 0:
                    q.append(c)
            
            # for c in graph[course]:

        return [x for x in range(n) if safe[x]]
        
            