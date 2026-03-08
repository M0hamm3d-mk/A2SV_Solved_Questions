def l709():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ops = []

    # ensure a[i] < b[i]
    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
            ops.append((3, i+1))

    # sort a
    for i in range(n):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                ops.append((1, j+1))

    # sort b 
    for i in range(n):
        for j in range(n-1-i):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
                ops.append((2, j+1))
    return [len(ops),  ops]
t = int(input())
for _ in range(t):
    res = l709()
    print(res[0])
    for i in res[1]:
        print(*i)