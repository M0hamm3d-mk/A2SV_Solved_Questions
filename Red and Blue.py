def redBlue():
    n = int(input())
    r = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    
    a = []
    # merge the two arrays and store them in a
    
    _sumr = _sumb = 0
    mr = mb = 0
    for i in range(n):
        _sumr += r[i]
        mr = max(mr,_sumr)
    for i in range(m):
        _sumb += b[i]
        mb = max(mb,_sumb)
        
    i = 0
    size = min(n,m)
    while i < size:
        a.append(r[i])
        a.append(b[i])
        i += 1
    a.extend(r[i:])
    a.extend(b[i:])
    maximum = 0
    pre = 0
    for i in range(m+n):
        pre += a[i]
        maximum = max(maximum,pre)
    return max(maximum,mr,mb,mr + mb)
t = int(input())
for _ in range(t):
    print(redBlue())
