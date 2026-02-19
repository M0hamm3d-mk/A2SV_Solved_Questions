class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)):
            curr = nums[i:i+3]
            if len(curr) >= 3:
                a,b,c = curr[0],curr[1],curr[2]
                if a + b > c and a + c > b and b + c > a:
                    return sum(curr)
        return 0
