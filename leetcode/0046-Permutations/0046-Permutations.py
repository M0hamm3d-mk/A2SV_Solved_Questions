class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        def backTrack(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return 
            for i in range(len(nums)):
                if nums[i] in seen: continue
                seen.add(nums[i])
                path.append(nums[i])
                backTrack(path)
                path.pop()
                seen.remove(nums[i])
        ans = []
        backTrack([])
        return ans