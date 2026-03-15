class Solution:
   
   
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = []
        mini = nums[0]
        for i in range(n):
            while stack and stack[-1][1] <= nums[i]:
                stack.pop()
                
            if  stack:
                if stack[-1][0] < nums[i] :
                    return True
            stack.append([mini,nums[i]])
            mini = min(mini,nums[i])
        return False