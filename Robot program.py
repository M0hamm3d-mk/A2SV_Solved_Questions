from collections import defaultdict,Counter
def robotProgram():
    n,x,k = map(int,input().split())
    s = input()
    for i in range(n):
        if s[i] == 'L':
            x -= 1
        else:
            x += 1
        k -= 1
        if x == 0:
            break
    res = 0
    if x == 0:
        res = 1
        for i in range(n):
            if s[i] == 'L':
                x -= 1
            else:
                x += 1
            if x == 0:
                return res + k//(i+1)
        return 1
    return 0
        
t = int(input())
for _ in range(t):
    print(robotProgram())
