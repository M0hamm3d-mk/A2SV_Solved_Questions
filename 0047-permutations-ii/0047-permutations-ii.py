class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        seen = set()
        def backTrack(path):
            if len(path) == len(nums) and tuple(path) not in seen:
                ans.append(path[:])
                seen.add(tuple(path))
                return 
            for i in range(len(nums)):
                if not used[i] : 
                    used[i] = True
                    path.append(nums[i])
                    backTrack(path)
                    path.pop()
                    used[i] = False
        ans = []
        backTrack([])
        return ans