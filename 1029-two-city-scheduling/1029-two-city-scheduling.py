class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costA = costB = 0
        a = b = 0
        costs.sort(key=lambda a:a[0] - a[1])
        for c in costs:
            if a + 1 > n // 2:
                break
            else:
                costA += c[0]
                a += 1
        for i in range(a,n):
            costB += costs[i][1]
        return costA + costB