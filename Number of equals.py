
def numberOfEqual():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    equals = 0
    i = j = 0

    while i < n and j < m:

        if a[i] == b[j]:
            count_a = count_b = 0
            curr = a[i]
            while i < n and a[i] == curr:
                count_a += 1
                i += 1
            while j < m and b[j] == curr:
                count_b += 1
                j += 1
            equals += count_a * count_b

        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return equals


print(numberOfEqual())
