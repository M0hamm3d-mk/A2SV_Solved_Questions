class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites:
            return True
        graph = defaultdict(list)

        for a,b in prerequisites:
            graph[a].append(b)

        color = [0] * numCourses
        # 0 not checked, 1 not taken -1 already taken

        def dfs(course):

            if color[course] == 1:
                return False

            elif color[course] == -1:
                return True

            color[course] = 1
            for pre in graph[course]:
                if not dfs(pre):
                    return False

            color[course] = -1
            return True

        for i  in range(numCourses):
            if not dfs(i):
                return False
                
        return True
            