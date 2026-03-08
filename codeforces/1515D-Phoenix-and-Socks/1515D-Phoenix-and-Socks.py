from collections import Counter


def phoenixAndSocks():
    n,l,r = map(int,input().split())
    socks = list(map(int,input().split()))
    
    
    left_counter = Counter(socks[:l])
    right_counter = Counter(socks[l:])
    left_socks = l
    right_socks = r
    
    # removig matching pairs without any cost
    for sock in left_counter:
        pair = min(left_counter[sock],right_counter[sock])
        
        left_counter[sock] -= pair
        right_counter[sock] -= pair
        
        left_socks -= pair
        right_socks -= pair
        
        n -= pair * 2
        
    # assume the right side remaining socks are the larger in size
    if left_socks >= right_socks:
        left_counter,right_counter = right_counter,left_counter
        left_socks,right_socks = right_socks,left_socks
        
    # first flip socks of the same color but in the same side to make them matching pair with cost of 1
    extra_socks = right_socks - left_socks
    flip_cost = 0
    for sock in right_counter:
        flip = min(right_counter[sock]//2, extra_socks//2) # for extra_socks we need only extra_socks // 2 flips
        flip_cost += flip
        extra_socks -= flip * 2
        n -= flip * 2
    
    # if there is left extra_socks 
    flip_cost += extra_socks // 2
    
    return flip_cost + n // 2
    
    
t = int(input())
for _ in range(t):
    print(phoenixAndSocks())