from collections import Counter


def needleInHaystack():
    s = input()
    t = list(input())
    counter_s = Counter(s)
    counter_t = Counter(t)

    for char in s:
        if counter_t[char] < counter_s[char]:
            return "Impossible"

    res = []
    keys = list(counter_t.keys())
    keys.sort()
    i = 0  
    for char in keys:
        while i < len(s) and s[i] <= char:
            res.append(s[i])
            i += 1
        res.extend([char] * (counter_t[char] - counter_s[char]))
    return "".join(res)


t = int(input())
for _ in range(t):
    print(needleInHaystack())
