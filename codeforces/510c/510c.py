from collections import defaultdict, deque


def solve():
    n = int(input())
    grid = []
    
    for _ in range(n):
        grid.append(input())
    
    
    indegree = defaultdict(int)
    graph = defaultdict(set)
    
    def compare(s,t): # compares two names and spot the order as well add one more child for the smaller character.returns boolean whether it is failed or not
        if s.startswith(t) and len(s) > len(t):
            return False
        i = 0
        while i < min(len(s),len(t)):
            if s[i] != t[i]:
                # if s[i] in graph[t[i]] or (graph[t[i]] and not graph[s[i]]): # checks if there is conflict 'Impossible' case
                #     return False
                graph[s[i]].add(t[i])
                return True
            i += 1
        return True
               
    for j in range(1,n): # check for one name against all except itself
        prev_name = grid[j-1]
        curr_name = grid[j]

        if not compare(prev_name,curr_name):
            return 'Impossible'
            
            
    for node in graph: # computing the indegree 
        for nei in graph[node]:
            indegree[nei] += 1
    # print(indegree)
    # print(graph)
    
    
    # BFS(TOPSORT)
    ans = []
    q = deque()
    for i in range(97,97+26):
        char = chr(i)
        if indegree[char] == 0:
            q.append(char)
    while q:
        node = q.popleft()
        ans.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if not indegree[nei]:
                q.append(nei)
    res = "".join(ans)
    if len(res) != 26:
        return 'Impossible'
    return res
print(solve())