def sociallyDistant():
    n = int(input())
    a = list(map(int,input().split()))
    res = [a[0]]
    
    if n == 1:
        return [1,a]
    
    rise = True
    if a[0] > a[1]:
        rise = False
    i = 1
    
    while i < n:
        
        while i < n and rise:
            if a[i] < a[i-1]:
                res.append(a[i-1])
                rise = False
            i += 1
        while i < n and not rise:
            if a[i] > a[i-1]:
                res.append(a[i-1])
                rise = True
            i += 1
        if i == n and rise:
            res.append(a[-1])
        if i == n and not rise:
            res.append(a[-1])
        
    return [len(res),res]


t = int(input())
for _ in range(t):
    ans = sociallyDistant()
    print(ans[0])
    print(*ans[1])
    
