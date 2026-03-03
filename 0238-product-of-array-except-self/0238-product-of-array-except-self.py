class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]
        post = [1]
        p = 1
        p2 = 1
        res = []

        for i in range(n):
            p *= nums[i]
            pre.append(p)
            p2 *= nums[-(i+1)]
            post.append(p2)

        post = post[::-1]
        res.append(pre[0] * post[1])
        
        for i in range(1,n):
            res.append(pre[i] * post[i+1])
        return res
        