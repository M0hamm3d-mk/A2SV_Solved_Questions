def segmentsWithSmallSet():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    memo = {}
    left = res = 0
    
    for right in range(n):
        memo[a[right]] = memo.get(a[right],0)+1
        while len(memo) > k:
            memo[a[left]] -= 1
            if memo[a[left]] == 0:
                del memo[a[left]]
            left += 1
        res += right - left + 1
    return res
print(segmentsWithSmallSet())
