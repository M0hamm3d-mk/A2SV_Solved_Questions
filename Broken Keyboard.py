def brokenKeyboard():
    s = input()
    n = len(s)
    if n == 1:
        return s
    i = 0
    working = []
    j = 1
    while i < n and j < n:
        if s[i] == s[j]:
            i = j + 1
            j += 2
        else:
            working.append(s[i])
            i = j
            j += 1
        if j == n and i != j:
            working.append(s[i])
            i += 1
    working = "".join((sorted(list(set(working)))))
    return working


t = int(input())
for _ in range(t):
    print(brokenKeyboard())
