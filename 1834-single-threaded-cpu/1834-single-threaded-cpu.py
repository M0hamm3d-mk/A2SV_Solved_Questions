class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for index,task in enumerate(tasks):
            task.append(index)
        
        tasks.sort()
        print(tasks)
        time = 1
        order = []
        i = 0
        min_heap = []
        while len(order) < n :

            while i < n and tasks[i][0] <= time:
                heappush(min_heap,(tasks[i][1],tasks[i][2]))
                i += 1

            if min_heap:
                completed = heappop(min_heap)
                order.append(completed[1])
                time += completed[0]
            else:
                time = tasks[i][0]
        return order
