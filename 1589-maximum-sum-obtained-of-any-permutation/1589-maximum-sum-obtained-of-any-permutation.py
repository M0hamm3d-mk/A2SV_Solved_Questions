class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        temp = sorted(nums)

        indexes = [0]*(n + 1)
        for start,end in requests:
            indexes[start] += 1
            indexes[end+1] -= 1

        pre = [0] * (n+1)
        pre[0] = indexes[0]
        for i in range(1,n+1):
            pre[i] = pre[i-1] + indexes[i]

        idx = []
        pre = pre[:n]
        for i,v in enumerate(pre):
            idx.append([i,v])

        idx.sort(key=lambda a:-a[1])
        for index,freq in idx:
            nums[index] = temp[-1]
            temp.pop()
    
        pre_sum = [0]*(n)
        pre_sum[0] = nums[0]
        for i in range(1,n):
            pre_sum[i] = pre_sum[i-1] + nums[i]

        res = 0
        pre_sum.append(0)
        for start,end in requests:
            if start == 0:
                res += pre_sum[end]
            else:
                res += pre_sum[end] - pre_sum[start-1]

        return res % (10 ** 9 + 7)
       
        