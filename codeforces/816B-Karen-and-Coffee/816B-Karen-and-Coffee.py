def karenNKoffee():
    n,k,q = map(int,input().split())
    difference_array = [0] * 200002
    for _ in range(n):
        l,r = map(int,input().split())
        difference_array[l] += 1
        difference_array[r+1] -= 1
    
    count = [0] * 200002
    for i in range(1,200002):
        count[i] = count[i-1] + difference_array[i]
        
    
    pre = [0] * 200002
    for i in range(1,200002):
        if count[i] >= k:
            pre[i] = pre[i-1] + 1
        else:
            pre[i] = pre[i-1] + 0
    
    for _ in range(q):
        l,r = map(int,input().split())
        print(pre[r]-pre[l-1])
        
karenNKoffee()