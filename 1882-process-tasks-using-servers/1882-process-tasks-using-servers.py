class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        m = len(tasks)
        ans = [0] * m

        free = [(servers[i], i) for i in range(n)]
        heapq.heapify(free)

        busy = []
        time = 0
        for j in range(m):
            time = max(time,j)

            if not free:
                time = busy[0][0]

            while busy and busy[0][0] <= time:
                finish, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx))

            weight, idx = heapq.heappop(free)
            ans[j] = idx
            heapq.heappush(busy, (time + tasks[j], weight, idx))

        return ans