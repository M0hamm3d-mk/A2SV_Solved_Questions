import sys
from collections import defaultdict, Counter, deque

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: "YES" if condition else "NO"

def solve():
    n = number()
    arr = listed()
    op = 0
    flag = False
    def conquer(left,right):
        nonlocal op
        nonlocal flag
        merged = []
        if left[-1] <= right[0]:
            merged =  left + right
        else:
            n = len(left)
            m = len(right)
            i = j = 0
            while i < n and j < m:
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            op += 1
            
        for k in range(1,len(left) + len(right)):
            if merged[k] - merged[k-1] > 1:
                flag = True
        return merged
    def divide(arr):
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        
        left = divide(arr[:mid])
        right = divide(arr[mid:])
        
        return conquer(left,right)
    
    
    divide(arr)
    return op if not flag else -1
        
test_cases = number()
for _ in range(test_cases):
    print(solve())