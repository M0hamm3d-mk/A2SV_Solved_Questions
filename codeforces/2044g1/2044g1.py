from collections import defaultdict, deque


def solve():
    n = int(input())
    a = list(map(int,input().split()))
    indegree = [0] * (n+1)
    graph = {}
    for i in range(n):
        indegree[a[i]] += 1
        graph[i+1] = a[i]

    q = deque()
    year = 2
    for i in range(1,n+1):
        if not indegree[i]:
            q.append(i)
    while q:
        
        for i in range(len(q)):
            node = q.popleft()
            v = graph[node]
            indegree[v] -= 1
            if not indegree[v]:
                q.append(v)
        year += 1
    return year
    
    
    
t = int(input())
for _ in range(t):
    print(solve())