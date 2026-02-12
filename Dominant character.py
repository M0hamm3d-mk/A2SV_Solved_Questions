from collections import Counter
def dominantChar():
    n = int(input())
    s = input()
    a,b,c,d,e,f,g,="aa", "aba", "aca", "abca", "acba", "abbacca", "accabba"
    if a in s:
        return 2
    if b in s or c in s :
        return 3
    if d in s or e in s:
        return 4
    if f in s or g in s:
        return 7
    else:
        return -1
t = int(input())
for _ in range(t):
    print(dominantChar())
