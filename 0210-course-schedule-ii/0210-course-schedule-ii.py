class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        indegree = [0] * (numCourses)
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        # print(indegree)
        # print(graph)

        q = deque()
        ans = []
        for i,j in enumerate(indegree):
            if j == 0:
                q.append(i)
        # print(q)

        while q:
            course = q.popleft()
            ans.append(course)

            for c in graph[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
            
            # for c in graph[course]:

        if len(ans) == numCourses:
            return ans

        return []
        
            