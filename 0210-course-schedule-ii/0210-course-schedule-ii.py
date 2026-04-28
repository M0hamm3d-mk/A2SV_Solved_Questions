class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for a,b in prerequisites:
            graph[b].append(a)

        color = [0] * numCourses
        # 0 not checked, 1 not taken -1 already taken
        res = []
        def dfs(course):

            if color[course] == 1:
                return False

            # elif color[course] == -1:
            #     return True

            color[course] = 1
            for pre in graph[course]:
                if color[pre] == -1:
                    continue
                if not dfs(pre):
                    return False

            color[course] = -1

            res.append(course)
            return True

        for i  in range(numCourses):
            if color[i] != -1:
                if not dfs(i):
                    return []
                    
        return res[::-1]
            