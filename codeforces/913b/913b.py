from collections import defaultdict, deque


def solve():
    n = int(input())
    
    graph = defaultdict(list)
    
    for i in range(n-1):
        graph[int(input())].append(i+2)
    # print(graph)
    
    queue = deque([1])
    
    while queue:
        node = queue.popleft()
        leaf = 0
        if  graph[node]:
            for nei in graph[node]:
                if not graph[nei]:
                    leaf += 1
                else:
                    queue.append(nei)
            if leaf < 3:
                return 'No'
    return 'Yes'
            
print(solve())