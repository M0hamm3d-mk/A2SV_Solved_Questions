def casino():
    
    n,k = map(int,input().split())
    _casino = []
    for _ in range(n):
        a = list(map(int,input().split()))
        a.sort()
        _casino.append(a)
    
    _casino.sort(key=lambda a:(a[0],-a[1]))
    
    for i in range(len(_casino)):
        
        if k < _casino[i][1]:
            if _casino[i][0] <= k <= _casino[i][2]:
                k = _casino[i][1]
    return k
t = int(input())
for _ in range(t):
    print(casino())
