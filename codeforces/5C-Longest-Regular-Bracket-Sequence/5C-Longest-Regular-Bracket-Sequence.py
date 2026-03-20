from collections import deque


def solve():
    s = input()
    lengths = []
    stack = []
    count = 0
    mx = 0
    d = {}
    op = []
    for i,v in enumerate(s):
        if v ==')':
            if op:
                d[op.pop()] = i
        else:
            op.append(i)
    ss = set(op) 
    # print(op)   
    for i in range(len(s)):
        if s[i] == '(' and i in ss:
            d[i] = -1
    # print(d)
    for i in range(len(s)):
        if s[i] == '(' and d[i] != -1:
            stack.append(i)
        else:
            if not stack:
                count = 0
            else:
                if s[ stack[-1]] == '(':
                    if d[stack[-1]] != -1:
                        count += 2
                        stack.pop()
                    else:
                        stack.pop()
                        lengths.append(count)
                        count = 0
                
                if not stack:
                    lengths.append(count)
    if stack:
        lengths.append(count)
    if lengths:
        mx = max(lengths)
    return f"{mx} {lengths.count(mx)}" if mx > 0 else f"0 1"

print(solve())



























# (()())()(())()()() ) () ) () (( () ( () ( () ) ()()() )   14  3 1  7