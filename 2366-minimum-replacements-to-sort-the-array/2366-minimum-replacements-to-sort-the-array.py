class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        op = 0
        temp = nums[::-1]
        smaller = temp[0]
        for i in range(1,n):
            if temp[i] > smaller:
                if temp[i] % smaller:
                    op += temp[i] // smaller
                    k = temp[i] / smaller
                    smaller = temp[i] // math.ceil(k)
                else:
                    op += temp[i] // smaller - 1
            else:
                smaller = temp[i]

        return op
