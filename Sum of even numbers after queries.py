class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_even = 0
        for i in nums:
            if i % 2 == 0:
                sum_even += i
        res = []
        for q in queries:
            curr = nums[q[1]]
            after = curr + q[0]
            nums[q[1]] = after
            if curr % 2 == 0:
                if after % 2 != 0:
                    sum_even -= curr
                else:
                    sum_even += q[0]
            else:
                if after % 2 == 0:
                    sum_even += after
            res.append(sum_even)
        return res
