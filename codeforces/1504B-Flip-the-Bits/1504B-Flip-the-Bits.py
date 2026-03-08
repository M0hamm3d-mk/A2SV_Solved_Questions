from typing import Counter


def flipBits():
    n = int(input())
    a = input()
    b = input()
    freq = Counter(a)
    ones = freq['1']
    zeros = freq['0']
    flipped = False
    i = n-1
    while i >= 0 :
        if not flipped and a[i] == b[i]:
            if a[i] == '1':
                ones -= 1
            else:
                zeros -= 1
            i -= 1
        elif not flipped and a[i] != b[i]:
            if zeros != ones:
                return 'NO'
            else:
                flipped = True
        elif flipped and a[i] != b[i]:
            if a[i] == '1':
                zeros -= 1
            else:
                ones -= 1
            i -= 1
        elif flipped and a[i] == b[i]:
            if zeros != ones:
                return 'NO'
            else:
                flipped = False
    return 'YES'
            


t = int(input())
for _ in range(t):
    print(flipBits())