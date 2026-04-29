class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        for source,destination in edges:
            graph[source].append(destination)
            indegree[destination] += 1
        ans = defaultdict(list)

        # print(graph)
        # print(indegree)
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        while q:

            node = q.popleft()

            for nei in graph[node]:
                indegree[nei] -= 1
                if ans[node]:
                    ans[nei].extend(ans[node])
                ans[nei].append(node)
                ans[nei] = (list(set(ans[nei])))
                if indegree[nei] == 0:
                    q.append(nei)
        return [sorted(ans[x]) for x in range(n)]