from collections import Counter

def longesKGoodSegments():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    freq = Counter()
    left = res = 0
    indexes = []
    
    for right in range(n):
        freq[a[right]] += 1
        
        while len(freq) > k:
            freq[a[left]] -= 1
            if freq[a[left]] == 0:
                del freq[a[left]]
            left += 1
        if right - left + 1 > res :
            res = right - left + 1
            indexes = [left+1,right+1]
    return indexes

print(*longesKGoodSegments())
    
            
