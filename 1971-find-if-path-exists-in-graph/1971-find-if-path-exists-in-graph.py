class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        edge_list = defaultdict(list)

        for u,v in edges:
            edge_list[u].append(v)
            edge_list[v].append(u)

        visited = [False] * n
        stack = [source]

        while stack:
            node = stack.pop()

            if node == destination:
                return True

            for neighbour in edge_list[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    stack.append(neighbour)
        return False
