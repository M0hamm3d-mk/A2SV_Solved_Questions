def solve():
    n,m = map(int,input().split())
    a = list( map(int,input().split()))
    b = list( map(int,input().split()))
    
    b.sort()
    # make the first element of a the smallest
    
    # low  = 0
    # high = m-1
    # while low <= high:
    #     mid = (low+high)//2
    #     if b[mid] - a[0] < a[0]:
    #         a[0] = b[mid] - a[0]
    #         high = mid - 1
    #     else:
    #         low = mid + 1
    
    a[0] = min(a[0], b[0] - a[0])
    for i in range(1,n):
        low  = 0
        high = m-1
        # print(a)
        if a[i] >= a[i-1]:
            curr = a[i]
            while low <= high:
                mid = (low+high)//2
                if b[mid] >= curr + a[i-1]:
                    a[i] = min(b[mid]-curr,a[i])
                    high = mid - 1
                else:
                    low = mid + 1
        else:
            curr = a[i]
            while low <= high:
                mid = (low+high)//2
                if b[mid] >= curr + a[i-1]:
                    a[i] = b[mid]-curr
                    high = mid - 1
                else:
                    low = mid + 1
        # print(a)
        if a[i] < a[i-1]:
            return 'NO'
    return 'YES'


t = int(input())
for _ in range(t):
    print(solve())