def blackAndWhite():
    n,k = map(int,input().split())
    s = input()
    freq = {'B':0,'W':0}
    
    for i in range(k):
        freq[s[i]] += 1
    res = freq['W']
    
    for r in range(k,n):
        freq[s[r]] += 1
        freq[s[r-k]] -= 1
        res = min(res,freq['W'])
        
    return res

t = int(input())
for _ in range(t):
    print(blackAndWhite())
    
