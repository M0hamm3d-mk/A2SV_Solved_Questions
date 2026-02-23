def arraySpliting():

    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    costs = []
    
    for i in range(n-1):
        costs.append(array[i+1]-array[i])
        
    return sum(sorted(costs)[:n-k])

print(arraySpliting())
