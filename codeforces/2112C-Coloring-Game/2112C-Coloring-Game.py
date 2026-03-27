def solve():
    n = int(input())
    a = list(map(int,input().split()))
    
    ways = 0
    mx = max(a)
    
    for i in range(2,n):
        
        target = max(a[i],mx-a[i])
        left = 0
        right = i-1
        
        while left < right:
            if a[left] + a[right] > target:
                ways += right - left
                right -= 1
            else:
                left += 1
    
    return ways


t = int(input())
for _ in range(t):
    print(solve())