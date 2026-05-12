class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n = len(tasks)
        m = len(servers)
        free = []
        for i in range(len(servers)):
            heappush(free,[servers[i],i])
        
        # print(free)
        busy = []
        ans = []
        time = 0
        i = 0  # task
        while i < n:
            
            # remove free servers from list of busy servers
            while busy and busy[0][0] <= time:
                heappush(free,heappop(busy)[1:])
            
            if free:
                w,idx = heappop(free)
                heappush(busy,[time + tasks[i],w,idx])
                i += 1
                ans.append(idx)
            else:
                time = busy[0][0]
            time = max(time,i)
        return ans

            



