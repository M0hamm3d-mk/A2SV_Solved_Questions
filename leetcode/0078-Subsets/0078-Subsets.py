class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(first,path):
            ans.append(path[:])
            for i in range(first,len(nums)):
                path.append(nums[i])
                helper(i+1,path)
                path.pop()
        ans = []
        helper(0,[])
        return ans