from collections import Counter
def polyCarp():
    n = int(input())
    a = list(map(int,input().split()))
    days = 0
    a.sort()
    freq = Counter(a)
    for i in range(n):
        if freq[a[i]] > 0 and a[i] > days:
            days += 1
            freq[a[i]] -= 1
    return days
print(polyCarp())
