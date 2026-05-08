class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        heap = []
        res = []
        for i,t in enumerate(tasks):
            t.append(i)
        k = 0
        t = 1
        # print(tasks)
        tasks.sort()
        while len(res) < n:
            while k < n and tasks[k][0] <= t:
                    heappush(heap,(tasks[k][1],tasks[k][2]))
                    k += 1
            if heap:
                curr = heappop(heap)
                res.append(curr[1])
                t += curr[0]
            else:
                t = tasks[k][0]
        return res