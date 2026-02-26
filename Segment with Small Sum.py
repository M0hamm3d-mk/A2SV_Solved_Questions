def segmentSum():
    n,s = map(int,input().split())
    a = list(map(int,input().split()))
    left = 0
    res = 0
    _sum = 0
    
    for right in range(n):
        _sum += a[right]
        while _sum > s:
            _sum -= a[left]
            left += 1
        
        res = max(res,right-left+1)
    return res
print(segmentSum())
