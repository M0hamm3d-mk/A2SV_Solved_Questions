from collections import defaultdict


def solve():
    n = int(input())
    graph = []
    
    for _ in range(n):
        graph.append(list(input()))
    
    after = [0] * (n+1)
    
    for i in range(n):
        for j in range(i+1,n):
            if graph[i][j] == '1':
                after[i+1] += 1
            else:
                after[j+1] += 1
    # print(after)
    p = [x for x in range(1,n+1)]
    
    p.sort(key=lambda a: (-after[a]))
    
    

    # print(p)
    
    return p
    
    
    
t = int(input())

for _ in range(t):
    print(*solve())