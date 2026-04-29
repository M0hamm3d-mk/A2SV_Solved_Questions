class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        parent = defaultdict(list)

        while q:
            course = q.popleft()
            for nei in graph[course]:
                indegree[nei] -= 1
                if parent[course]:
                    parent[nei].extend(set(parent[course]))
                parent[nei].append(course)
                if indegree[nei] == 0:
                    q.append(nei)
        for i in range(len(parent)):
            parent[i] = set(parent[i])
        ans = []
        for u,v in queries:
            if u in parent[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans


