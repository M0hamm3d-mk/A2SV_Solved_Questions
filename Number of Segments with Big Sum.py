def segmentsWithBigSum():

    n,s = map(int,input().split())
    a = list(map(int,input().split()))
    if min(a) >= s:
        return n* (n+1) // 2
    if sum(a) < s:
        return 0
    total = 0
    _sum = 0
    left = 0
    for i in range(n):
        _sum += a[i]
        while _sum >= s:
           _sum -= a[left]
           left += 1
        total += (i-left + 1)
 
    return (n*(n+1)//2) - total
print(segmentsWithBigSum())
